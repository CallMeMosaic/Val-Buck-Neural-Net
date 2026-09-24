from dataclasses import dataclass

from fundamentals.Signal import Signal
from fundamentals.transmitters import Transmitters
from fundamentals.transmitters_cost import TransmittersCost


@dataclass
class NeuroTransmitter:
    """
    Primary class for neurotransmitters

    :type: dataclass
    :param nt_type: Transmitter type.
    :param value: Transmitter value (for interactions within neurons).


    :author: CallMeMosaic
    :since: 0.0.1
    :version: 0.0.1

    """

    def __init__(
            self,
            nt_type: Transmitters,
            cost: TransmittersCost,
            signal: Signal

    ):
        self.nt_type = nt_type
        self.cost = cost
        self.signal = signal
