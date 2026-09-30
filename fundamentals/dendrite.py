from numbers import Number

import math
from math import sqrt

from fundamentals.control.time import Time
from fundamentals.dendrite_branch import DendriteBranch
from fundamentals.maths.CONSTANTS import DELTA_T
from fundamentals.mitochondrion import Mitochondrion
from fundamentals.neuron_dna import NeuronDNA
from fundamentals.transmitters import Transmitters


class Dendrite:
    """
    Represents the Dendrite, the first processing layer of the neuron.
    It gathers all charge/input from its connecting dendritic branches and applies
    spatial and temporal decay functions to it before checking if it can fire.
    Hereby the dendrite can act as a first layer of computation before the soma.
    If the charge threshold is met, a dendrite can fire and relay its charge to the soma.
    A Dendrite also provides all necessary properties for spatial and temporal decay as well as
    methods to create and remove dendritic branches.


    :param mitochondrion: Mitochondrion: The mitochondrion supplying energy for the dendrite's operations.
    :param local_threshold: float: The minimum local charge threshold needed to fire.
    :param baseline_charge: float: The baseline charge of the dendrite. After each fire, the charge resets to this value.
    :param branches: List[DendriteBranch]: The list of dendrite branches connected to the dendrite. Charges will be accumulated from them.
    :param global_time: Time: The global time object is used for time-based calculations. POSSIBLY OBSOLETE?
    :param width: int: The width of the dendrite, used for cable theory calculations.
    :param length: int: The length of the dendrite, used for cable theory calculations.
    :param membrane_resistance: float: The resistance of the dendrite's membrane. Necessary for cable theory calculations.


    Late-Initialized Properties:
    :property internal_resistance: Float: Internal resistance of the axon to charge dissipating.
    :property space_constant: Float: The square root of the membrane resistance divided by the axon's internal resistance. Indicates how much percentage of charge dissipates over one length unit.
    :property cable_area: Float: The surface area of the axon. It is calculated as the product of the axon's width and length.
    :property membrane_capacitance: Float: How much the membrane stores/absorbs charge over the length of the axon.
    :property tau_membrane: Float: The time constant of the membrane, calculated as the product of the membrane resistance and membrane capacitance.
    :property attenuation_factor: Float:
    :property time_scaling_factor: Float:


    :author: CallMeMosaic
    :since: 0.0.1
    :version: 0.0.4


    Changelog:
    - 0.0.3: Added spatial and temporal decay properties and did some formatting.

    - 0.0.4: Final formatting.
    """

    def __init__(
            self,
            mitochondrion: Mitochondrion,
            local_threshold: float = -44,
            # mV Minimum local charge necessary for a local spike -> Soma | Should be around -52 to -41 mV
            baseline_charge: float = -70,
            # Determines the base charge, so the current charge can also be reset to this | Should be around -75 to -60 mV
            branches=None,  # All the branches of the dendrite
            # activation_function: ActivationFunction = ReLu, # Activation Function passed so each dendrite can have its own
            global_time=Time,
            width: int = 1,
            length: int = 1,
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

        if length is not None:
            if not isinstance(length, Number) or isinstance(length, bool):
                raise TypeError("Length must be of type Number!")
            else:
                if length <= 0:
                    raise ValueError("Length must be greater than 0!")
                length = int(length)
        else:
            raise ValueError("Length cannot be None!")

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

        if not isinstance(mitochondrion, Mitochondrion) or mitochondrion is None:
            raise TypeError("Mitochondrion must be instance of type Mitochondrion!")

        self.mitochondrion = mitochondrion


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


        # Ensure membrane_resistance passes the type hints and is reasonable

        if not isinstance(membrane_resistance, Number) or isinstance(membrane_resistance, bool):
            raise TypeError("Membrane resistance must be a number")
        else:
            membrane_resistance = float(membrane_resistance)

        self.membrane_resistance = membrane_resistance


        # Add charge to dendrite

        charge: float = baseline_charge
        self.charge = charge


        # Values for cable theory DO THIS WITH DNA LATER

        self.internal_resistance = 10 / width

        self.space_constant = sqrt(membrane_resistance / self.internal_resistance)

        self.cable_area = width * length * math.pi

        self.membrane_capacitance = 1.0 * self.cable_area

        self.tau_membrane = self.membrane_capacitance * membrane_resistance

        self.attenuation_factor = math.exp(-length / self.space_constant)

        self.leak_factor = math.exp(-(DELTA_T / self.tau_membrane))

        self.time_scaling_factor = (DELTA_T / self.tau_membrane)

    """
    ————————————————————————————————————————————————————————————————————————————————————————————————————————————————
    """

    def create_and_add_branch(self,
                              receptor_type: Transmitters,
                              branch_dna: NeuronDNA,
                              length: int = 1,
                              width: int = 1,
                              membrane_resistance: int = 20000):
        """
        Creates a new dendritic branch and adds it to the list of branches. The new branch is initialized
        with a specific length, transmitter receptor type, and a target axon terminal. Important note, the branch is created and appended inside this method.
        There is no method to only create a branch and not append it to the list, as branches should not be created without being appended or having a connection.



        :param receptor_type: Transmitters: The type of transmitter the branch will use.
        :param branch_dna: NeuronDNA: The DNA of the branch.
        :param length: int: The length of the branch, used for cable theory calculations.
        :param width: int: The width of the branch, used for cable theory calculations.
        :param membrane_resistance: int: The resistance of the branch's membrane.


        :return: None
        """

        self.branches.append(DendriteBranch(None,
                                            Mitochondrion(),
                                            receptor_type,
                                            branch_dna,
                                            length,
                                            width,
                                            membrane_resistance))

    """
    ————————————————————————————————————————————————————————————————————————————————————————————————————————————————
    """

    def remove_and_delete_branch(self, branch: DendriteBranch):
        """
        Removes a specified branch from the collection of branches and deletes it.


        :param branch: DendriteBranch: The branch object to be removed and deleted.
        :return: None
        """

        self.branches.remove(branch)
