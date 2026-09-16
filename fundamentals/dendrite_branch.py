from numbers import Number
from typing import Optional

from errorhandling.neuron_exceptions import NeuronDNAError
from fundamentals.Signal import Signal
from fundamentals.axon_terminal import AxonTerminal
from fundamentals.mitochondrion import Mitochondrion
from fundamentals.neuro_transmitter import NeuroTransmitter
from fundamentals.neuron_dna import NeuronDNA
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
                 Also added parameter for dna of soma, so no branch can be build that would accept invalid signals (neuron cancer? I mean biologically it is possible probalby???)
                 Added width parameter for spatial decay calculation.
                 Added Mitochondrion parameter for energy consumption.
    """
    def __init__(
            self,
            current_signal: Signal,
            mitochondrion: Mitochondrion, # The Powerhouse of each cell innit
            receptor_type: Transmitters,  # From transmitters enum
            branch_dna: NeuronDNA, # Ensures that the Branches cannot receive signals from neurons that use different Neuro Transmitters
            length: float = 1.0, # default value is 1.0, needed for spatial decay calculation
            width: float = 1.0, # default value is 1.0, needed for spatial decay calculation
            name: Optional[str] = None, # Optional name for easier debugging
    ):
        # Ensure current Signal follows type hints
        if not isinstance(current_signal, Signal) or current_signal is None:
            raise TypeError("current_signal must instance of class Signal")

        self.current_signal = current_signal


        # Ensure the DNA passes type hints
        if not isinstance(branch_dna, NeuronDNA) or branch_dna is None:
            raise TypeError("branch_dna must instance of class NeuronDNA")

        self.branch_dna = branch_dna


        # Ensure Mitochondrion passes type hints
        if not isinstance(mitochondrion, Mitochondrion) or mitochondrion is None:
            raise TypeError("mitochondrion must instance of class Mitochondrion")

        self.mitochondrion = mitochondrion


        # Ensure the current receptor type matches the DNA
        if not isinstance(receptor_type, Transmitters) or receptor_type is None:
            raise TypeError("receptor_type must instance of class Transmitters")

        if branch_dna.allowed_receptors != receptor_type:
            raise NeuronDNAError(module=self, expected=branch_dna.allowed_receptors, actual=receptor_type)

        self.receptor_type = receptor_type


        # Ensure length passes type hint and is reasonable
        if not isinstance(length, Number) or isinstance(length, bool):
            raise TypeError("Length must be a number")
        else:
            length = float(length)

        if length <= 0:
            raise ValueError("Length must be greater than 0")

        self.length = length


        # Ensure width passes type hint and is reasonable
        if not isinstance(width, Number) or isinstance(width, bool):
            raise TypeError("Width must be a number")
        else:
            width = float(width)

        if width <= 0:
            raise ValueError("Width must be greater than 0")

        self.width = width



    def receive_signal(self, acceptor: NeuroTransmitter, ) -> bool:
        # Basically accepts a Neuro Transmitter object and reduces it to the signal object
        """
        Primary function of this class.
        Accepts a NeuroTransmitter object and deletes the NeuroTransmitter and only keeps the Signal object carried by it.
        1. Checks first if its Mitochondrion can handle the current action, if not, the Neurotransmitter will be rejected and destroyed by the Synapse.
        2. Checks if the Transmitter Types match, if not, it refuses but still has depleted energy.
        3. Applies cable theory to the signal for the traveled distance.
        4. Saves a Signal object and returns the state of the operation.


        :param acceptor: NeuroTransmitter object = The NeuroTransmitter passed on by the synapse.
        :return: Boolean = True if Signal was accepted, False if not.
        """


        if self.mitochondrion.consume(acceptor.cost):

            if acceptor.nt_type == self.receptor_type:



            else:
                return False

        else:
            return False

        self.current_Signal = acceptor.signal



        #TODO: Make sure NT object is handled correctly here
        #TODO: Add cable theory
