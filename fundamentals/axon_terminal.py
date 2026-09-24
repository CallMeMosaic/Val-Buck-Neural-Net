import math
from math import sqrt
from numbers import Number

from fundamentals.Signal import Signal
from fundamentals.maths.CONSTANTS import DELTA_T
from fundamentals.mitochondrion import Mitochondrion
from fundamentals.neuro_transmitter import NeuroTransmitter
from fundamentals.synapse import Synapse
from fundamentals.transmitters import Transmitters
from fundamentals.transmitters_cost import TransmittersCost


class AxonTerminal:
    """
    Represents the terminal structure of an axon in a neural network model.

    This class defines an axon terminal, which is responsible for transmitting neurotransmitters
    of a specific type to a linked it's dedicated synapse. It includes all necessary properties to calculate
    spatial decay via the cable theory function and hands its synthesized Neuro Transmitter to its linked Synapse.

    :param synapse: Synapse: The synapse to which this axon terminal is linked.
    :param mitochondrion: Mitochondrion: The mitochondrion responsible for energy management.
    :param synthesis_type: Transmitters: The type of neurotransmitter synthesized by this axon terminal.
    :param length: int: Length of the axon terminal, used for cable theory. Must be greater than 0.
    :param width: int: Width of the axon terminal, used for cable theory. Must be greater than 0.
    :param membrane_resistance: float: The resistance of the axon terminal's membrane. Also used for cable theory. Must be greater than 0.

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
    - 0.0.2: Total rework of the entire class. Added cable theory-related properties, cleaned out old properties, and structured code and documentation to look better and be more readable.
             Also added a synthesis method.
    """

    def __init__(self,
                 synapse: Synapse,
                 # Non-optional as an axon terminal should not exist without a synapse, since that would mean it would fire to nowhere.
                 mitochondrion: Mitochondrion,
                 synthesis_type: Transmitters,
                 length: int = 1,
                 width: int = 1,
                 membrane_resistance: float = 1.0):

        # Ensure Synapse exists and is according to Type Hint

        if not isinstance(synapse, Synapse) or synapse is None:
            raise TypeError("Synapse must be instance of class Synapse and cannot be None!")

        self.synapse = synapse

        # Ensure the Mitochondrion is not none or not of type mitochondrion

        if not isinstance(mitochondrion, Mitochondrion) or mitochondrion is None:
            raise TypeError("Mitochondrion must be instance of type Mitochondrion!")

        self.mitochondrion = mitochondrion

        # Ensure Synthesis Type is according to Type Hint

        if not isinstance(synthesis_type, Transmitters):
            raise TypeError("Synthesis Type must be value of Transmitters enum!")

        self.synthesis_type = synthesis_type

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

        # Ensure Width is according to Type Hints

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

        # Ensure Membrane Resistance is according to Type Hints

        if not isinstance(membrane_resistance, Number) or isinstance(membrane_resistance, bool):
            raise TypeError("Membrane resistance must be a number")
        else:
            membrane_resistance = float(membrane_resistance)

        self.membrane_resistance = membrane_resistance

        # Create Terminal Queue

        self.terminal_queue = []

        # Values for cable Theory DO THIS WITH DNA LATER

        self.internal_resistance = 10 / width

        self.space_constant = sqrt(membrane_resistance / self.internal_resistance)

        self.cable_area = width * length * math.pi

        self.membrane_capacitance = 1.0 * self.cable_area  # Sure that taking it times one makes sense?

        self.tau_membrane = self.membrane_capacitance * self.internal_resistance

        self.attenuation_factor = math.exp(-length / self.space_constant)

        self.time_scaling_factor = (DELTA_T / self.tau_membrane)

    """
    ————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
    """

    def synthesize(self, value: float) -> NeuroTransmitter:
        """
        Method to synthesize a new neurotransmitter object.
        Takes the value of the signal from outside (soma process method) and integrates it into a new signal object nested inside a neuro transmitter object.

        :param value: Float: The value of the signal to be synthesized. Usually the propagated action potential from the soma.
        :return NeuroTransmitter: The newly synthesized neuro transmitter object.
        """

        return NeuroTransmitter(self.synthesis_type,
                                TransmittersCost(self.synthesis_type.value.capitalize()),
                                Signal(value))


    """
    ————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
    """

    def process_queue
