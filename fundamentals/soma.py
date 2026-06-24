from typing import Optional, Tuple

from fundamentals.Signal import Signal
from fundamentals.axon import Axon
from fundamentals.dendrite import Dendrite
from fundamentals.mitochondrion import Mitochondrion
from fundamentals.nucleus import Nucleus
from fundamentals.transmitters import Transmitters
from fundamentals.transmitters_cost import TransmittersCost


class Soma:
    """
    Represents the Soma, the cell body of a neuron, responsible for integration and processing of
    incoming signals. It interfaces with dendrites, an axon, a mitochondrion for energy supply,
    and a nucleus for genetic material. Soma processes signals and generates outgoing signals
    when needed, considering its threshold and refractory state.

    :ivar axon: The axon is connected to the Soma, responsible for transmitting outgoing signals.
    :type axon: Axon
    :ivar dendrites: A list of dendrites connected to the Soma, responsible for receiving incoming signals.
    :type dendrites: list[Dendrite]
    :ivar name: Optional name of the Soma to distinguish it, if required.
    :type name: Optional[str]
    :ivar mitochondrion: The mitochondrion supplying energy for the Soma's operations.
    :type mitochondrion: Mitochondrion
    :ivar nucleus: The nucleus containing genetic material and regulating Soma functions.
    :type nucleus: Nucleus
    :ivar threshold: The minimum energy threshold needed to process an incoming signal.
    :type threshold: Float
    :ivar refractory_period: Period during which the Soma cannot fire another signal after processing one.
    :type refractory_period: Float
    :ivar is_exhausted: A boolean flag indicating whether the Soma is in an exhausted state, unable to process signals.
    :type is_exhausted: Bool
    :ivar refractory_timer: Tracks the remaining time in the Soma's refractory period.
    :type refractory_timer: Int

    :author: CallMeMosaic
    :since: 0.0.1
    :version: 0.0.1
    """
    def __init__(
            self,
            axon: Axon,
            dendrites: list[Dendrite],
            mitochondrion: Mitochondrion,
            nucleus: Nucleus,
            threshold: float = 0.5,
            refractory_period: float = 0.5,
            name: Optional[str] = None,
    ):
        # Axon and Dendrites need to nullable so a Soma can also be created without them (initial creation)
        self.axon = axon
        self.dendrites = dendrites
        self.name = name

        if mitochondrion is None:
            raise ValueError("Mitochondrion cannot be None")
        self.mitochondrion = mitochondrion

        if nucleus is None:
            raise ValueError("Nucleus cannot be None")
        self.nucleus = nucleus

        if threshold <= 0:
            raise ValueError("Threshold must be greater than 0")
        self.threshold = threshold

        if refractory_period <= 0:
            raise ValueError("Refractory period must be greater than 0")
        self.refractory_period = refractory_period

        # Needed to determine if the soma needs to enter Blackout state
        is_exhausted = False
        self.is_exhausted = is_exhausted

        # Needed to check if the Soma is in a refractory period or not
        refractory_timer = 1
        self.refractory_timer = refractory_timer

        # Needed to

    def process(self, incoming: Signal) -> Signal | None:
        # TODO: - Implement this
        # TODO: Should use the data contained in the NeuroTransmitter and process it
        # TODO: RUN CHECK UP ON MITOCHONDRION

        if self.mitochondrion.current_charge < self.threshold:
            is_exhausted = True
            return None

        if self.refractory_timer > 0:
            self.refractory_timer -= 1
            # Still do the maths, but with don't fire
            return None

        else:
            if self.mitochondrion.consume(TransmittersCost.STANDARD):
                # DO Maths here
                outgoing = Signal(2)  # PLACEHOLDER
                return outgoing
            else:
                # Save the signal for later?
                return None

    def assign_transmitter(self, signal: Signal) -> Tuple[Transmitters, TransmittersCost]:
        # TODO: - Implement this
        # TODO: Should use the Signal returned from the process method to assign a transmitter and return said transmitter
        # TODO: RETURN TYPE IS CROOKED
        # TODO: RUN CHECK UP ON MITOCHONDRION

        self.mitochondrion.consume(TransmittersCost.STANDARD)
        transmitter_tuple: Tuple
        return transmitter_tuple[Transmitters, TransmittersCost]

    def fire(self):
        self.mitochondrion.consume(TransmittersCost.FIRE)
        # TODO: -implement this
        # TODO: Should command the firing of the transmitter
        pass
