from typing import Optional

from fundamentals.Signal import Signal
from fundamentals.axon_terminal import AxonTerminal
from fundamentals.neuro_transmitter import NeuroTransmitter
from fundamentals.transmitters import Transmitters


class DendriteBranch:
    """
    Represents a dendrite branch in a neural network model.

    This class provides the structure and functionality to model a dendritic branch
    that connects to an axon terminal, facilitating neural communication. The dendrite
    branch is characterized by its length, the type of neurotransmitter receptor it contains,
    and the axon terminal it is connected to. Its primary function is to receive signals
    transmitted by the connected axon terminal.

    :ivar parent_axon_terminal: The axon terminal connected to the dendrite branch.
    :type parent_axon_terminal: AxonTerminal
    :ivar length: The length of the dendrite branch. It must be greater than 0.
    :type length: float
    :ivar receptor_type: The type of neurotransmitter receptor contained in the
        dendrite branch. Must match the transmitter type of the connected axon terminal.
    :type receptor_type: Transmitters

    :author: CallMeMosaic
    :since: 0.0.1
    :version: 0.0.2

    Changelog:
        - 0.0.2: Added proper type hints and removed unnecessary stuff
    """
    def __init__(
            self,
            length: float = 1.0,  # default value is 1.0, needed for calculations later
            receptor_type: Transmitters = None,  # From transmitters enum
            parent_axon_terminal: AxonTerminal = None,
            # Makes sure that the axon terminal's type matches the receptor type
            name: Optional[str] = None, # Optional name for easier debugging
            current_signal: Signal = None,
            current_NT: Transmitters = None, # The Neuro Transmitter type that was handed to the Branch
            last_NT: Transmitters = None, # For applying effects and tracking in Dendrite
    ):
        if length <= 0:
            raise ValueError("Length must be greater than 0")
        if receptor_type not in Transmitters:
            raise ValueError("Invalid receptor type")
        if receptor_type != parent_axon_terminal.effector_type:
            raise ValueError(f"Transmitter mismatch: Dendrite expects: {receptor_type}, "
                             f" but connecting axon sends: {parent_axon_terminal.effector_type}")
        if parent_axon_terminal is None:
            raise ValueError("Parent axon terminal cannot be None")

        # Make sure current NT is of the correct types
        if current_NT is not None or NeuroTransmitter:
            raise ValueError("NeuroTransmitter cannot be used with current_NT")
        self.current_NT = current_NT

        # Same thing for the last NT
        if last_NT is not None or NeuroTransmitter:
            raise ValueError("NeuroTransmitter cannot be used with last_NT")
        self.last_NT = last_NT

        self.parent_axon_terminal = parent_axon_terminal
        self.length = length
        self.receptor_type = receptor_type
        self.current_Signal = current_signal



    def receive_signal(self, acceptor: NeuroTransmitter, ):
        # Basically accepts a Neuro Transmitter object and reduces it to the signal object
        """

        :param acceptor:
        :return:
        """
        self.current_Signal = acceptor.signal
        self.last_NT = self.current_NT


        #TODO:  Apply Bias and Weight here
        #TODO: Make sure NT object is handled correctly here
        #TODO: Add cable theory
