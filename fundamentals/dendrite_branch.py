import math

from math import sqrt
from numbers import Number
from typing import Optional

from errorhandling.neuron_exceptions import NeuronDNAError
from fundamentals.Signal import Signal
from fundamentals.maths.CONSTANTS import DELTA_T
from fundamentals.mitochondrion import Mitochondrion
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

    # TODO: ADD LINKED SYNAPSE!!!
    def __init__(
            self,
            current_signal: Signal | None,
            mitochondrion: Mitochondrion, # The Powerhouse of each cell innit
            receptor_type: Transmitters,  # From transmitters enum
            branch_dna: NeuronDNA, # Ensures that the Branches cannot receive signals from neurons that use different Neuro Transmitters
            length: int = 1, # default value is 1.0, needed for spatial decay calculation
            width: int = 1, # default value is 1.0, needed for spatial decay calculation
            membrane_resistance: float = 1.0,
            name: Optional[str] = None, # Optional name for easier debugging
    ):
        # Ensure current Signal follows type hints, Can be None as it is set to none when signal is processed
        if current_signal is not None and not isinstance(current_signal, Signal):
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


        # Ensure length passes a type hint and is reasonable
        if not isinstance(length, Number) or isinstance(length, bool):
            raise TypeError("Length must be a number")
        else:
            length = int(length)

        if length <= 0:
            raise ValueError("Length must be greater than 0")

        self.length = length


        # Ensure width passes type hint and is reasonable
        if not isinstance(width, Number) or isinstance(width, bool):
            raise TypeError("Width must be a number")
        else:
            width = int(width)

        if width <= 0:
            raise ValueError("Width must be greater than 0")

        self.width = width

        if not isinstance(membrane_resistance, Number) or isinstance(membrane_resistance, bool):
            raise TypeError("Membrane resistance must be a number")
        else:
            membrane_resistance = float(membrane_resistance)

        self.membrane_resistance = membrane_resistance

        # Values for cable theory DO THIS WITH DNA LATER

        self.internal_resistance = 10 / width

        self.space_constant = sqrt(membrane_resistance / self.internal_resistance)

        self.cable_area = width * length * math.pi

        self.membrane_capacitance = 1.0 * self.cable_area

        self.tau_membrane = self.membrane_capacitance * membrane_resistance

        self.attenuation_factor = math.exp(-length / self.space_constant)

        self.time_scaling_factor = (DELTA_T / self.tau_membrane)


        #TODO:



