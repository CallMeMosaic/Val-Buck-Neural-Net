from fundamentals.axon_terminal import AxonTerminal
from fundamentals.dendrite_branch import DendriteBranch
from fundamentals.synaptic_membrane import SynapticMembrane


class Synapse:
    def __init__(
            self,
            weight: float,
            membrane: SynapticMembrane,
            terminal: AxonTerminal,
            branch: DendriteBranch
    ):
        if weight <= 0 or weight is None:
            if weight is not float:
                raise ValueError("Weight must be a float")
            else:
                raise ValueError("Weight must be greater than 0")
        self.weight = weight

        if membrane is None or membrane is not SynapticMembrane:
            raise ValueError("Membrane must be object of type SynapticMembrane!")
        self.membrane = membrane

        if terminal is None or terminal is not AxonTerminal:
            raise ValueError("Terminal must be object of type AxonTerminal!")
        self.terminal = terminal

        if branch is None or branch is not DendriteBranch:
            raise ValueError("Branch must be object of type DendriteBranch!")
        self.branch = branch
