import math

from math import sqrt
from numbers import Number
from typing import List, Callable

#from fundamentals import mitochondrion # Double import and shadow?? Wtf?
from fundamentals.axon_terminal import AxonTerminal
from fundamentals.dendrite_branch import DendriteBranch
from fundamentals.maths.CONSTANTS import DELTA_T
from fundamentals.maths.activation_functions import ReLu, ActivationFunction
from fundamentals.mitochondrion import Mitochondrion
from fundamentals.soma import Soma
from fundamentals.transmitters import Transmitters
from fundamentals.transmitters_cost import TransmittersCost
from fundamentals.control.time import Time


#TODO: - Dendritic pre-processing
#TODO: - Needs to be non linear (Activation Function)
#TODO - Needs relay to Soma ASAP



class Dendrite:
    """
    Represents a dendrite, a part of a neuron that receives signals from other neurons and relays
    them to its cell body. The class manages its length, associated mitochondrion, and functionality
    to handle dendritic branches and accepted neurotransmitters.

    Dendrites are critical parts of neural signaling, and this class provides methods to
    dynamically create, append, and remove dendritic branches, while ensuring valid initialization
    and attribute settings.

    :ivar length: The length of the dendrite in the neural structure.
    :type length: Float
    :ivar mitochondrion: Is The mitochondrion associated with the dendritic structure.
    :type mitochondrion: Mitochondrion
    :ivar accepted_transmitters: A list of transmitters accepted by the dendrite.
    :type accepted_transmitters: List[Transmitters]
    :ivar branches: A collection of dendritic branches created dynamically.
    :type branches: List[DendriteBranch]

    :author: CallMeMosaic
    :since: 0.0.1
    :version: 0.0.3
    """
    def __init__(
            self,
            mitochondrion: Mitochondrion,
            related_soma: Soma,  # Needed for handing off the processed value to the soma
            local_threshold: float = -44, # mV Minimum local charge necessary for a local spike -> Soma | Should be around -52 to -41 mV
            baseline_charge: float = -70, # Determines the base charge, so current charge can also be reset to this | Should be around -75 to -60 mV
            branches= None, # All the branches of the dendrite
            activation_function: ActivationFunction = ReLu,# Activation Function passed so each dendrite can have its own
            global_time = Time,
            width: int = 1.0,
            length: int = 1.0,
            membrane_resistance: float = 1.0,

    ):
        # Ensure branches are existent
        if branches is None or not isinstance(branches, list):
            raise TypeError("Dendrite must have at least one branch to function!")

        for branch in branches:
            if not isinstance(branch, DendriteBranch):
                raise TypeError("Branches must be instance of DendriteBranch!")

        self.branches = branches


        # Ensure the length is greater than 0 and is according to type hint.
        if not isinstance(length, float) or length is None:
            raise TypeError("Length must be of type float!")

        if length <= 0:
            raise ValueError("Length must be greater than 0!")

        self.length = length


        # Ensure the width is greater than 0 and is according to type hint.

        if width is not None:
            if not isinstance(width, Number) or isinstance(width, bool):
                raise TypeError("Width must be of type Number!")
            else:
                if width <= 0:
                    raise ValueError("Width must be greater than 0!")
                width = int(width)
        else:
            raise ValueError("Width cannot be None!")

        self.width = width


        # Ensure the Mitochondrion is not none or not of type mitochondrion

        if not isinstance(mitochondrion,Mitochondrion) or mitochondrion is None:
            raise TypeError("Mitochondrion must be instance of type Mitochondrion!")

        self.mitochondrion = mitochondrion


        # Ensure the Soma is not none or not of type soma
        if not isinstance(related_soma, Soma) or related_soma is None:
            raise TypeError("Soma must be instance of type Soma!")

        self.related_soma = related_soma


        # Ensure local_threshold is within reasonable parameters and of type float
        if not isinstance(local_threshold, Number) or isinstance(local_threshold, bool):
            raise TypeError("Baseline charge must be of type float!")

        if local_threshold < -52.0 or local_threshold > -41.0:
            raise ValueError("Baseline charge must be within interval of -52.0 and -41.0!")

        self.local_threshold = local_threshold

        # Ensure baseline_charge is within reasonable parameters and of type float
        if not isinstance(baseline_charge, Number) or isinstance(baseline_charge, bool):
            raise TypeError("Baseline charge must be of type float!")

        if baseline_charge < -75.0 or baseline_charge > -60.0:
            raise ValueError("Baseline charge must be within interval of -75.0 and -60.0!")

        self.baseline_charge = baseline_charge


        # Ensure time is of type Time
        if not isinstance(global_time, Time) or global_time is None:
            raise TypeError("Global time must be of type Time!")

        self.global_time: Time = global_time


        # Ensure activation function is callable
        if not isinstance(activation_function, ActivationFunction):
            raise TypeError("Activation function must be of type ActivationFunction!")

        self.activation_function: Callable
        self.activation_function = activation_function.calculate

        # Dynamic Properties necessary to keep track of dendrite branches and transmitters
        self.accepted_transmitters: List[Transmitters] = []
        self.branches: List[DendriteBranch] = []

        # Add charge to neuron
        charge: float = baseline_charge
        self.charge = charge


        # Ensure length passes a type hint and is reasonable
        if not isinstance(length, Number) or isinstance(length, bool):
            raise TypeError("Length must be a number")
        else:
            length = int(length)

        if length <= 0:
            raise ValueError("Length must be greater than 0")

        self.length = length


        # Ensure width passes type hint and is reasonable
        if not isinstance(width, Number) or isinstance(width, bool):
            raise TypeError("Width must be a number")
        else:
            width = int(width)

        if width <= 0:
            raise ValueError("Width must be greater than 0")

        self.width = width

        if not isinstance(membrane_resistance, Number) or isinstance(membrane_resistance, bool):
            raise TypeError("Membrane resistance must be a number")
        else:
            membrane_resistance = float(membrane_resistance)

        self.membrane_resistance = membrane_resistance

        # Values for cable theory DO THIS WITH DNA LATER

        self.internal_resistance = 10 / width

        self.space_constant = sqrt(membrane_resistance / self.internal_resistance)

        self.cable_area = width * length * math.pi

        self.membrane_capacitance = 1.0 * self.cable_area

        self.tau_membrane = self.membrane_capacitance * membrane_resistance

        self.attenuation_factor = math.exp(-length / self.space_constant)

        self.time_scaling_factor = (DELTA_T / self.tau_membrane)


    def create_and_add_branch(self, length: float, receptor_type: Transmitters, target_axon_terminal: AxonTerminal):
        """
        Creates a new dendritic branch and adds it to the list of branches. The new branch is initialised
        with a specific length, transmitter receptor type, and a target axon terminal. Important note, the branch is created and appended inside this method.
        There is no method to only create a branch and not append it to the list, as branches should not be created without being appended or having a connection.


        :param self: The instance of the class where the method is being called.
        :param length: The length of the new dendritic branch.
        :type length: Float
        :param receptor_type: The neurotransmitter receptor type associated with the new branch.
        :type receptor_type: Transmitters
        :param target_axon_terminal: The target axon terminal to which the new branch is connected.
        :type target_axon_terminal: AxonTerminal
        :return: None
        """

        self.branches.append(DendriteBranch(length, receptor_type, target_axon_terminal))

    def remove_and_delete_branch(self, branch: DendriteBranch):
        """
        Removes a specified branch from the collection of branches and deletes it.

        :param branch: The branch object to be removed and deleted.
        :type branch: DendriteBranch
        :return: None
        """
        self.branches.remove(branch)