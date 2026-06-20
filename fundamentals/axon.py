from fundamentals.Signal import Signal
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


    def synthesize(self,transmitter: Transmitters, cost: TransmittersCost, signal: Signal) -> NeuroTransmitter | None:
        # Check if the transmitter can be synthesized
        if not self.nucleus.dna.can_synthesise(transmitter):
            raise ValueError(f"Transmitter {transmitter} cannot be synthesized")
        if self.mitochondrion.consume(cost):
            return NeuroTransmitter(transmitter,cost, signal)
        else:
            pass