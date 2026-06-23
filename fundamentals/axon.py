from typing import List

from fundamentals.Signal import Signal
from fundamentals.axon_terminal import AxonTerminal
from fundamentals.mitochondrion import Mitochondrion
from fundamentals.neuro_transmitter import NeuroTransmitter
from fundamentals.nucleus import Nucleus
from fundamentals.transmitters import Transmitters
from fundamentals.transmitters_cost import TransmittersCost


class Axon:

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
        # Check if the transmitter can be synthesized
        if not self.nucleus.dna.can_synthesise(transmitter):
            raise ValueError(f"Transmitter {transmitter} cannot be synthesized")
        if self.mitochondrion.consume(cost):
            return NeuroTransmitter(transmitter,cost, signal)
        else:
            return None


    def add_terminal(self, terminal: AxonTerminal):
        self.axon_terminals.append(terminal)
