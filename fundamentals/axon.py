import math
from math import sqrt
from numbers import Number
from typing import List

from fundamentals.Signal import Signal
from fundamentals.axon_terminal import AxonTerminal
from fundamentals.dendrite_branch import DendriteBranch
from fundamentals.maths.CONSTANTS import DELTA_T
from fundamentals.mitochondrion import Mitochondrion
from fundamentals.neuro_transmitter import NeuroTransmitter
from fundamentals.nucleus import Nucleus
from fundamentals.transmitters import Transmitters
from fundamentals.transmitters_cost import TransmittersCost


class Axon:
    """
    Represents the axon of the neuron, responsible for transmitting the action potential of the soma to the exon terminals.
    Mostly needed for applying cable theory function inside the soma, to simulate the action potential propagation.

    :param current_charge: Float: Current charge of the axon. Is set to 0 by default.
    :param width: Int: Width of the axon. The default value is 1.
    :param length: Int: Length of the axon. The default value is 1.
    :param membrane_resistance: Float: Membrane resistance of the axon. Is set to 1.0 by default as it does not affect the cable theory equations.
    :param axon_terminals: List[AxonTerminal]: List of axon terminals connected to the axon.

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
    :version: 0.0.2


    Changelog:
    - 0.0.2: Fully reworked the axon class to include all necessary parameters for the maths and calculations.
             Also added proper documentation and proper type hints and type enforcement.
    """
#TODO: YEAH WE SHOULD DO SOMETHING HERE RIGHT?


    def __init__(self,
                 current_charge: float = 0,
                 width: int = 1,
                 length: int = 1,
                 membrane_resistance: float = 1.0,
                 axon_terminals: list[AxonTerminal] = None,
                 ):


        # Ensure current charge is according to type hints

        if not isinstance(current_charge, Number) or isinstance(current_charge, bool):
            raise TypeError("Current Charge of Axon needs to be instance of class Number and not bool")

        if current_charge > 0:
            raise ValueError("Current Charge of Axon needs to be non-positive")

        self.current_charge = int(current_charge)


        # Ensure width is according to type hints

        if not isinstance(width, Number) or isinstance(width, bool):
            raise TypeError("Width of Axon needs to be instance of class Number and not bool")

        if width <= 0:
            raise ValueError("Width of Axon needs to be greater than 0")

        self.width = int(width)


        # Ensure length is according to type hints

        if not isinstance(length, Number) or isinstance(length, bool):
            raise TypeError("Length of Axon needs to be instance of class Number and not bool")

        if length <= 0:
            raise ValueError("Length of Axon needs to be greater than 0")

        self.length = int(length)


        # Ensure Membrane Resistance is according to type hints

        if not isinstance(membrane_resistance, Number) or isinstance(membrane_resistance, bool):
            raise TypeError("Membrane Resistance needs to be instance of class Number and not bool")

        if membrane_resistance <= 0:
            raise ValueError("Membrane Resistance needs to be greater than 0")

        self.membrane_resistance = int(membrane_resistance)


        # Ensure Axon Terminals are according to type hint

        if not isinstance(axon_terminals, list):
            raise TypeError("Axon Terminals needs to be instance of clas List")

        for at in axon_terminals:
            if not isinstance(at, AxonTerminal):
                raise TypeError("Axon Terminals inside Axon Terminal list need to be instances of class AxonTerminal")

        self.axon_terminals = axon_terminals


        # Values for cable Theory DO THIS WITH DNA LATER

        self.internal_resistance = 10 / width

        self.space_constant = sqrt(membrane_resistance / self.internal_resistance)

        self.cable_area = width * length * math.pi

        self.membrane_capacitance = 1.0 * self.cable_area # Sure that taking it times one makes sense?

        self.tau_membrane = self.membrane_capacitance * self.internal_resistance

        self.attenuation_factor = math.exp(-length / self.space_constant)

        self.time_scaling_factor = (DELTA_T / self.tau_membrane)



    """
    ————————————————————————————————————————————————————————————————————————————————————————————————————————————————
    """


    def create_and_add_terminal(self, affector_type: Transmitters, linked_dendrite_branch: DendriteBranch,
                                length: float):
        """
        Creates and adds an axon terminal to the current list of axon terminals within the neuron.

        This method instantiates a new `AxonTerminal` object with the provided parameters and appends it
        to the axon terminal list, associating it with the neuron instance.

        :param affector_type: The type of neurotransmitter used by the axon terminal.
        :type affector_type: Transmitters
        :param linked_dendrite_branch: The dendrite branch that this axon terminal will link to for signal transmission.
        :type linked_dendrite_branch: DendriteBranch
        :param length: The length of the axon terminal, determining its physical extension.
        :type length: float
        :return: None
        """
        self.axon_terminals.append(AxonTerminal(self, affector_type, linked_dendrite_branch, length))

    def remove_terminal(self, terminal: AxonTerminal):
        self.axon_terminals.remove(terminal)
