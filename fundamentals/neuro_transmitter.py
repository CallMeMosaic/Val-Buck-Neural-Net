from dataclasses import dataclass

from fundamentals.Signal import Signal
from fundamentals.transmitters_cost import TransmittersCost
from transmitters import Transmitters

@dataclass
class NeuroTransmitter:
    """
    Primary class for neurotransmitters

    :type: dataclass
    :param type: Transmitter type.
    :param value: Transmitter value (for interactions within neurons).


    :author: CallMeMosaic
    :since: 0.0.1
    :version: 0.0.1

    """
    def __init__(
        self,
        type: Transmitters,
        cost: TransmittersCost,
        signal: Signal

    ):
        self.type = type
        self.cost = cost
        self.signal = signal
