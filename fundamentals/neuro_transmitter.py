from dataclasses import dataclass

from fundamentals.Signal import Signal
from fundamentals.transmitters import Transmitters
from fundamentals.transmitters_cost import TransmittersCost


@dataclass
class NeuroTransmitter:
    """
    Class representing a Neuro Transmitter object. Used inside the Neural Network to pass forth charges.
    Carries a Signal object, its own type and the cost it has to be received.


    :param nt_type: Transmitters: A Value of the Transmtters enum, used for comparison when synthesizing or receiving
    Neuro Transmitters.
    :param cost: TransmittersCost: A Value of the TransmittersCost enum, used to ensure that only valid numbers are entered
    and later for determining how much the receiving of this Neuro Transmitter costs.
    :param signal: Signal: A Signal object carrying the charge transmitted by the Neuro Transmitter.


    :author: CallMeMosaic
    :since: 0.0.1
    :version: 0.0.2


    Changelog:
    - 0.0.2: Changed Documentation and type hint enforcement.

    """

    def __init__(
            self,
            nt_type: Transmitters,
            cost: TransmittersCost,
            signal: Signal

    ):

        # Ensure nt_type is according to type hints

        if not nt_type is None:

            if isinstance(nt_type, Transmitters):

                self.nt_type = nt_type

            else:
                raise TypeError("nt_type needs to be value from Transmitters enum!")

        else:
            raise TypeError("nt_type cannot be None!")


        # Ensure cost is according to type hints

        if not cost is None:

            if isinstance(cost, TransmittersCost):

                self.cost = cost

            else:
                raise TypeError("Cost of Neuro Transmitter must be value of TransmittersCost enum!")

        else:
            raise TypeError("Cost of Neuro Transmitter cannot be None!")


        # Ensure signal is according to type hints

        if not signal is None:

            if isinstance(signal, Signal):

                self.signal = signal

            else:
                raise TypeError("Signal of Neuro Transmitter must be instance of class Signal!")

        else:
            raise TypeError("Signal cannot be None!")
