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


    def __init__(self,
                 mitochondrion: Mitochondrion,
                 synthesis_type: Transmitters,
                 length: int = 1,
                 width: int = 1,
                 membrane_resistance: float = 1.0):


        # Ensure the Mitochondrion is not none or not of type mitochondrion

        if not isinstance(mitochondrion,Mitochondrion) or mitochondrion is None:
            raise TypeError("Mitochondrion must be instance of type Mitochondrion!")

        self.mitochondrion = mitochondrion


        # Ensure Synthesis Type is according to Type Hint

        if not isinstance(synthesis_type, Transmitters):
            raise TypeError("Synthesis Type must be value of Transmitters enum!")

        self.synthesis_type = synthesis_type


        # Ensure the length is greater than 0 and is according to type hint.

        if length is not None:
            if not isinstance(length, Number) or isinstance(length, bool):
                raise TypeError("Length must be of type Number!")
            else:
                if length <= 0:
                    raise ValueError("Length must be greater than 0!")
                length = int(length)
        else:
            raise ValueError("Length cannot be None!")

        self.length = length

        # Ensure Width is according to Type Hints

        if width is not None:
            if not isinstance(width, Number) or isinstance(width, bool):
                raise TypeError("Width must be of type Number!")
            else:
                if width <= 0:
                    raise ValueError("Width must be greater than 0!")
                width = int(width)
        else:
            raise ValueError("Width cannot be None!")

        self.width = width


        # Ensure Membrane Resistance is according to Type Hints

        if not isinstance(membrane_resistance, Number) or isinstance(membrane_resistance, bool):
            raise TypeError("Membrane resistance must be a number")
        else:
            membrane_resistance = float(membrane_resistance)

        self.membrane_resistance = membrane_resistance


        # Create Terminal Queue

        self.terminal_queue = []


        # Values for cable Theory DO THIS WITH DNA LATER

        self.internal_resistance = 10 / width

        self.space_constant = sqrt(membrane_resistance / self.internal_resistance)

        self.cable_area = width * length * math.pi

        self.membrane_capacitance = 1.0 * self.cable_area # Sure that taking it times one makes sense?

        self.tau_membrane = self.membrane_capacitance * self.internal_resistance

        self.attenuation_factor = math.exp(-length / self.space_constant)

        self.time_scaling_factor = (DELTA_T / self.tau_membrane)



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

        if effector_type not in Transmitters or effector_type is None or effector_type not in parent_axon.nucleus.dna.allowed_syntheses:
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
