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
                 Also added parameter for dna of soma, so no branch can be build that would accept invalid signals (neuron cancer? I mean biologically it is possible probalby???)
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
            current_signal: Signal = None,
            current_NT: Transmitters = None, # The Neuro Transmitter type that was handed to the Branch
            last_NT: Transmitters = None, # For applying effects and tracking in Dendrite
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


        # Ensure parent axon terminal passes type hint
        if not isinstance(parent_axon_terminal, AxonTerminal) or parent_axon_terminal is None:
            raise TypeError("Parent axon terminal must be an instance of class AxonTerminal")



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
