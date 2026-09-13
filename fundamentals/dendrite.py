from typing import List, Callable

#from fundamentals import mitochondrion # Double import and shadow?? Wtf?
from fundamentals.axon_terminal import AxonTerminal
from fundamentals.dendrite_branch import DendriteBranch
from fundamentals.maths.activation_functions import ReLu
from fundamentals.mitochondrion import Mitochondrion
from fundamentals.soma import Soma
from fundamentals.transmitters import Transmitters
from fundamentals.transmitters_cost import TransmittersCost


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
    :version: 0.0.2
    """
    def __init__(
            self,
            mitochondrion: Mitochondrion,
            related_soma: Soma,  # Needed for handing off the processed value to the soma
            length: float = 1.0, # default value is 1.0
            local_threshold: float = -44, # mV Minimum local charge necessary for a local spike -> Soma
            baseline_charge: float = -70, # Determines the base charge, so current charge can also be reset to this
            activation_function: Callable = ReLu # Activation Function passed so each dendrite can have it's own

    ):
        # Ensure the length makes sense
        if length <= 0 or length is None or length is not float:
            raise ValueError("Length must be greater than 0 and of type float")
        self.length = length

        # Ensure the Mitochondrion is not none or not of type mitochondrion
        if mitochondrion is None or mitochondrion is not Mitochondrion:
            raise ValueError("Mitochondrion must be object of type Mitochondrion!")
        self.mitochondrion = mitochondrion

        # Ensure the Soma is not none or not of type soma
        if related_soma is None or related_soma is not Soma:
            raise ValueError("Soma must be object of type Soma!")
        self.related_soma = related_soma

        # Dynamic Properties necessary to keep track of dendrite branches and transmitters
        self.accepted_transmitters: List[Transmitters] = []
        self.branches: List[DendriteBranch] = []

        # Add charge to neuron
        charge: float = -70 # mV
        self.charge = charge

        #Add Baseline Charge: TODO: - Add a way to ensure that this baseline charge is within reasonable parameters!!!
        self.baseline_charge: float = baseline_charge

        # Make sure local threshold is usable TODO: - Add way to ensure this threshold is within reasonable parameters!!!
        self.local_threshold = local_threshold

        self.activation_function = activation_function

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


    def fire(self):

        """

        :return:
        """

        # Step 1: Check if firing is possible, by checking in on the mitochondrion
        if self.mitochondrion.consume(TransmittersCost.FIRE):
            if self.charge >= self.local_threshold:
                # For now use difference between threshold and actual charge as signal value to hand off
                self.related_soma.process(abs(self.local_threshold - self.charge))
        else:
            print("CANNOT FIRE: MITOCHONDRION IS EXHAUSTED")





    def process_branches(self):
        """
        Applies the passed activation function to the values received by each dendrite branch.
        This prepares the values for evaluation.
        Also summarizes all the values held inside the dendrite branches' current signals, to the current charge.
        If a branch's signal has been added to the charge of the dendrite, its reference is destroyed, so it can be collected by GC.
        This also ensures that no Signal can be processed twice.


        :return:
        """
        for branch in self.branches:

            # Step 1: Add signal value to charge in a loop
            branch.current_Signal.value = self.activation_function(branch.current_Signal.value)

            # Step 2: Add the processed signal value to the dendrite branch's charge level
            self.charge += branch.current_Signal.value

            # Step 3: Reduce the local Mitochondrion energy, be the amount of the Signal's NT
            self.mitochondrion.consume(TransmittersCost(branch.current_NT.name))

            # Step 4: Remove the reference to the signal object, so GC collects it
            branch.current_Signal = None

            #TODO: Add cable theory

        # # Step 5: Outside of Loop, check if the charge is high enough after the processing
        # if self.charge >= self.local_threshold:
        #     self.charge = self.baseline_charge
        #     return True
        #
        # return False

