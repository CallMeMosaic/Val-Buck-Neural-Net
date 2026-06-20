from typing import List, Dict, Optional, Tuple
import numpy as np
from fundamentals.axon_terminal import AxonTerminal
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
    :version: 0.0.1
    """
    def __init__(
            self,
            length: float, # default value is 1.0, needed for calculations later
            receptor_type: Transmitters, # From transmitters enum
            parent_axon_terminal: AxonTerminal, # Makes sure that the axon terminal's type matches the receptor type
            name: Optional[str] = None # Optional name for easier debugging
    ):
        if length <= 0:
            raise ValueError("Length must be greater than 0")
        if receptor_type not in Transmitters:
            raise ValueError("Invalid receptor type")
        if receptor_type != parent_axon_terminal.type:
            raise ValueError(f"Transmitter mismatch: Dendrite expexts: {receptor_type}, "
                             f" but connecting axon sends: {parent_axon_terminal.type}")
        if parent_axon_terminal is None:
            raise ValueError("Parent axon terminal cannot be None")

        self.parent_axon_terminal = parent_axon_terminal
        self.length = length
        self.receptor_type = receptor_type

    # def receive_signal(
    #         self,
    #
    # ):
