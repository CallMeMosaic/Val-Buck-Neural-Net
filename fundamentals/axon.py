from typing import List

from fundamentals.Signal import Signal
from fundamentals.axon_terminal import AxonTerminal
from fundamentals.dendrite_branch import DendriteBranch
from fundamentals.mitochondrion import Mitochondrion
from fundamentals.neuro_transmitter import NeuroTransmitter
from fundamentals.nucleus import Nucleus
from fundamentals.transmitters import Transmitters
from fundamentals.transmitters_cost import TransmittersCost


class Axon:
    """
    Represents an axon, a key structure of a neuron responsible for
    transmitting information to other neurons through axon terminals.

    The Axon class manages the key biological components necessary for
    synaptic neurotransmitter synthesis and axon terminal operations.

    :ivar nucleus: The nucleus associated with the axon is responsible for
        controlling its operations and synthesizing neurotransmitters.
    :type nucleus: Nucleus
    :ivar mitochondrion: The mitochondrion associated with the axon
        providing energy for neurotransmitter synthesis and other activities.
    :type mitochondrion: Mitochondrion
    :ivar axon_terminals: A list of attached axon terminals for transmitting
        signals to other neurons.
    :type axon_terminals: List[AxonTerminal]

    :author: CallMeMosaic
    :since: 0.0.1
    :version: 0.0.1
    """

    def __init__(self,
                 nucleus: Nucleus,
                 mitochondrion: Mitochondrion

                 ):
        if nucleus is None:
            raise ValueError("Nucleus cannot be None")
        self.nucleus = nucleus

        if mitochondrion is None:
            raise ValueError("Mitochondrion cannot be None")
        self.mitochondrion = mitochondrion

        # List of axon terminals
        self.axon_terminals: List[AxonTerminal] = []


    def synthesize(self,transmitter: Transmitters, cost: TransmittersCost, signal: Signal) -> NeuroTransmitter | None:
        """
        Synthesise a neurotransmitter based on the given transmitter, its cost, and the signal to
        create. This process checks if the DNA within the nucleus allows synthesising the provided
        transmitter. If allowed, it verifies whether the mitochondrion can produce sufficient energy
        to create the neurotransmitter. Upon successful synthesis, a `NeuroTransmitter` object is
        created and returned; otherwise, it returns None.

        :param transmitter: The transmitter to be synthesised.
        :param cost: The energy cost associated with synthesising the transmitter.
        :param signal: The signal associated with this neurotransmitter.
        :return: A `NeuroTransmitter` object if synthesis is successful, None otherwise.
        """

        # Check if the transmitter can be synthesised

        if not self.nucleus.dna.can_synthesise(transmitter):
            raise ValueError(f"Transmitter {transmitter} cannot be synthesized")
        if self.mitochondrion.consume(cost):
            return NeuroTransmitter(transmitter,cost, signal)
        else:
            return None

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
