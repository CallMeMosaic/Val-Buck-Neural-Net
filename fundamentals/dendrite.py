from typing import List

from fundamentals.axon_terminal import AxonTerminal
from fundamentals.dendrite_branch import DendriteBranch
from fundamentals.mitochondrion import Mitochondrion
from fundamentals.transmitters import Transmitters

#TODO: - Dendritic pre-processing
#TODO: - Needs to be non linear (Activation Function)



class Dendrite:
    """
    Represents a dendrite, a part of a neuron that receives signals from other neurons and relays
    them to its cell body. The class manages its length, associated mitochondrion, and functionality
    to handle dendritic branches and accepted neurotransmitters.

    Dendrites are critical components of neural signalling, and this class provides methods to
    dynamically create, append, and remove dendritic branches, while ensuring valid initialisation
    and attribute settings.

    :ivar length: The length of the dendrite in the neural structure.
    :type length: Float
    :ivar mitochondrion: The mitochondrion associated with the dendritic structure.
    :type mitochondrion: Mitochondrion
    :ivar accepted_transmitters: A list of transmitters accepted by the dendrite.
    :type accepted_transmitters: List[Transmitters]
    :ivar branches: A collection of dendritic branches created dynamically.
    :type branches: List[DendriteBranch]

    :author: CallMeMosaic
    :since: 0.0.1
    :version: 0.0.1
    """
    def __init__(
            self,
            mitochondrion: Mitochondrion,
            length: float = 1.0, # default value is 1.0

    ):
        if length <= 0 or length is None or length is not float:
            raise ValueError("Length must be greater than 0 and of type float")
        self.length = length

        if mitochondrion is None or mitochondrion is not Mitochondrion:
            raise ValueError("Mitochondrion must be object of type Mitochondrion!")
        self.mitochondrion = mitochondrion

        # Dynamic Properties necessary to keep track of dendrite branches and transmitters
        self.accepted_transmitters: List[Transmitters] = []
        self.branches: List[DendriteBranch] = []

    def create_and_add_branch(self, length: float, receptor_type: Transmitters, target_axon_terminal: AxonTerminal):
        """
        Creates a new dendritic branch and adds it to the list of branches. The new branch is initialised
        with a specific length, transmitter receptor type, and a target axon terminal. Important note, the branch is created and appended inside this method.
        There is no method to only create a branch and not append it to the list, as branches should not be created without being appended or having a connection.


        :param self: The instance of the class where the method is being called.
        :param length: The length of the new dendritic branch.
        :type length: Float
        :param receptor_type: The neurotransmitter receptor type associated with the new branch.
        :type receptor_type: Transmitters
        :param target_axon_terminal: The target axon terminal to which the new branch is connected.
        :type target_axon_terminal: AxonTerminal
        :return: None
        """
        self.branches.append(DendriteBranch(length, receptor_type, target_axon_terminal))

    def remove_and_delete_branch(self, branch: DendriteBranch):
        """
        Removes a specified branch from the collection of branches and deletes it.

        :param branch: The branch object to be removed and deleted.
        :type branch: DendriteBranch
        :return: None
        """
        self.branches.remove(branch)
