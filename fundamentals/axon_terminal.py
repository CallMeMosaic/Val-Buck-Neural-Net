from typing import Optional

from fundamentals.axon import Axon
from fundamentals.dendrite_branch import DendriteBranch
from fundamentals.transmitters import Transmitters


class AxonTerminal:
    """
    Represents the terminal structure of an axon in a neural network model.

    This class defines an axon terminal, which is responsible for transmitting neurotransmitters
    of a specific type to a linked dendrite branch. It ensures constraints such as the correct
    type of parent axon, neurotransmitter type, and linkage with dendrite branches. It also
    supports naming for better identification in debugging scenarios.

    :ivar length: Length of the axon terminal, used for neural network-related calculations.
        Must be greater than 0.
    :type length: Float
    :ivar effector_type: Type of neurotransmitter (NT) this axon terminal can fire.
        Must be a valid entry in the allowed synthesizes of the parent axon's nucleus DNA.
    :type effector_type: Transmitters
    :ivar parent_axon: The parent axon object to which this terminal is linked.
    :type parent_axon: Axon
    :ivar linked_dendrite_branch: The dendrite branch to which this axon terminal is connected.
        Handles the continuation of the signal in the neural network.
    :type linked_dendrite_branch: DendriteBranch
    :ivar name: An optional name for the axon terminal, useful for debugging.
    :type name: Optional[str]

    :author: CallMeMosaic
    :since: 0.0.1
    :version: 0.0.1
    """
    def __init__(
            self,
            parent_axon: Axon,  # Linked parent axon, important for checking the type of NTs and using its methods
            effector_type: Transmitters,  # As one axon terminal can only fire one type of NT
            linked_dendrite_branch: DendriteBranch,  # Link to the following dendrite branch.
            length: float = 1.0,  # Default value is 1.0, needed for calculations later
            name: Optional[str] = None  # Optional name for easier debugging
    ):
        if length <= 0 or length is None:
            raise ValueError("Length must be greater than 0 and cannot be None")
        self.length = length

        if effector_type not in Transmitters or effector_type is None or effector_type not in parent_axon.nucleus.dna.allowed_synthesises:
            raise ValueError(f"Invalid effector type: {effector_type}")
        self.effector_type = effector_type

        if parent_axon is None or parent_axon is not Axon:
            raise ValueError("Parent axon must be object of type Axon!")
        self.parent_axon = parent_axon

        if linked_dendrite_branch is None or linked_dendrite_branch is not DendriteBranch:
            raise ValueError("Linked dendrite branch must be object of type DendriteBranch!")
        self.linked_dendrite_branch = linked_dendrite_branch

        self.name = name

    def fire(self):
        pass
