from fundamentals.neuro_transmitter import NeuroTransmitter
from fundamentals.transmitters import Transmitters


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
    :ivar allowed_synthesises: A list of neurotransmitters that the neuron can
                               synthesize.
    :type allowed_syntheses: Tuple[Transmitters]

    :author: CallMeMosaic
    :since: 0.0.1
    :version: 0.0.1
    """
    def __init__(
            self,
            allowed_receptors: tuple[Transmitters], # Determines which Transmitters the neuron can receive
            allowed_syntheses: tuple[Transmitters] # Determines which Transmitters the neuron can synthesize
    ):
        # Check if the lists are not empty
        if allowed_receptors is None:
            raise ValueError("Allowed receptors cannot be None")
        # Check if the lists are not empty
        if len(allowed_receptors) == 0:
            raise ValueError("Allowed receptors cannot be empty")
        if len(allowed_syntheses) == 0:
            raise ValueError("Allowed synthesises cannot be empty")
        # Check if the lists are not None
        if allowed_syntheses is None:
            raise ValueError("Allowed synthesises cannot be None")

        # Only then assign the lists
        self.allowed_receptors = allowed_receptors
        self.allowed_synthesises = allowed_syntheses

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
        return transmitter in self.allowed_synthesises

#TODO: MAKE TUPLES PROPERTIES VIA @PROPTERY TO PREVENT THEM FROM EXTERNAL MODIFICATION