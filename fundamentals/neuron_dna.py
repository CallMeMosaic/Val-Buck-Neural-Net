from numbers import Number

from fundamentals import transmitters
from fundamentals.control.time import Time
from fundamentals.neuro_transmitter import NeuroTransmitter
from fundamentals.transmitters import Transmitters

# TODO: THIS NEEDS TO INCLUDE ALL CONFIG DATA FOR AN ENTIRE NEURON.

#@dataclass(frozen=True) # Makes the instance immutable
class NeuronDNA:

    """
    Represents the DNA structure for a neuron, defining its allowed interactions
    with specific neurotransmitters.

    This class encapsulates the genetic blueprint of a neuron, specifying which
    neurotransmitters it can receive and synthesize. It provides methods to check
    for these capabilities. The primary purpose of this class is to model
    neurobiological interactions in a computational environment.

    :ivar allowed_receptors: A list of neurotransmitters that the neuron can
                             receive.
    :type allowed_receptors: Tuple[Transmitters]
    :ivar allowed_syntheses: A list of neurotransmitters that the neuron can
                               synthesize.
    :type allowed_syntheses: Tuple[Transmitters]

    :author: CallMeMosaic
    :since: 0.0.1
    :version: 0.0.1
    """

    #TODO: OPTZIMIZE THIS ESPECIALLY WITH TYPING AND DESIGN
    def __init__(
            self,
            allowed_receptors: Transmitters, # Determines which Transmitters the neuron can receive
            allowed_syntheses: Transmitters,# Determines which Transmitters the neuron can synthesize
            signal_frequency: float, # Determines the frequency of the neuron's signal
            global_time: Time, # References the internal clock so that each neuron can access it in every method without needing parameters for it.
    ):
        # Check if allowed_receptors is according to type hint
        if not isinstance(allowed_receptors,Transmitters):
            raise ValueError("Allowed receptors needs part of Transmitters enum")


        if not isinstance(allowed_syntheses,Transmitters):
            raise ValueError("Allowed synthesis needs to be part of Tranmitters enum")

        self.allowed_receptors = allowed_receptors

        self.allowed_syntheses = allowed_syntheses


        # Check if signal frequency is according to type hint
        if not isinstance(signal_frequency,Number) or isinstance(signal_frequency, bool):
            if not float(signal_frequency):
                raise ValueError("Signal frequency needs to be a at least a number!")
            else:
                signal_frequency = float(signal_frequency)

        if float(signal_frequency) <= 0:
            raise ValueError("Signal frequency needs to be a positive number!")

        self.signal_frequency = signal_frequency


        # Type Check for global_time
        if not isinstance(global_time, Time):
            raise TypeError("Global time needs to be an instance of Time!")

        self.global_time = global_time



    def can_receive(self, transmitter: NeuroTransmitter) -> bool:
        """
        Determines if a given transmitter is part of the allowed receptors.

        This method checks whether the provided transmitter is in the list of
        allowed receptors for the current object. The function returns a boolean
        indicating the result of this check.

        :param transmitter: The transmitter to be verified.
        :type transmitter: Transmitters
        :return: True if the transmitter is part of the allowed receptors,
            otherwise False.
        :rtype: Bool
        """
        return transmitter.type in self.allowed_receptors

    def can_synthesise(self, transmitter: Transmitters) -> bool:
        """
        Determines if the given transmitter can be synthesized.

        This method checks if the provided transmitter is included in the list of allowed synthesizable
        transmitters. It returns a boolean indicating whether the transmitter can be synthesized or not.

        :param transmitter: The transmitter to check for synthesis capability.
        :type transmitter: Transmitters
        :return: A boolean indicating if the transmitter can be synthesized.
        :rtype: Bool
        """
        return transmitter in self.allowed_syntheses

#TODO: MAKE TUPLES PROPERTIES VIA @PROPTERY TO PREVENT THEM FROM EXTERNAL MODIFICATION
#TODO: FIX NONABLE ISSUE
#TODO: DNA IS THE CONFIG FILE ~Alyssa