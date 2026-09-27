import math

from fundamentals.axon_terminal import AxonTerminal
from fundamentals.dendrite_branch import DendriteBranch
from fundamentals.maths.CONSTANTS import SYNAPSE_TAU_MEMBRANE, DELTA_T, SYNAPSE_OVERCHARGE_THRESHOLD
from fundamentals.maths.lif_model import lif_model
from fundamentals.neuro_transmitter import NeuroTransmitter
from fundamentals.synaptic_membrane import SynapticMembrane

#TODO: Membrane should have resistence which should be deducted from the signal.
#TODO: THIS CLASS NEEDS TO DELETE THE PRIOR REFERENCES, SO GC CAN COLLLECT THEM.
#TODO: NT MUST BE DESTROYED AS IF DENDRITE BRACH REFUSES IT.
#TODO: SUCCESSFUL TRANMISSION NEEDS TO STRENGTHEN THE SYNAPSE. AKA LOWER MEMBRANE RESISTANCE.


class Synapse:
    def __init__(
            self,
            weight: float,
            membrane: SynapticMembrane,
            terminal: AxonTerminal,
            branch: DendriteBranch,
            current_signal: NeuroTransmitter,
            residual_charge: float
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

        self.current_signal = current_signal

        self.leak_factor = 1 / weight # Inverses the weight to keep modulation for leak

        self.residual_charge = residual_charge

        self.leak_factor = math.exp(-DELTA_T / SYNAPSE_TAU_MEMBRANE)

    def calculate_and_strip(self):
        # BRANCH CAN REFUSE, SO IF THAT HAPPENS CHARGE GATHERS AND GETS LEAKIED IN THEIR ARSE

        # Apply weight to modulate the signal's value
        self.current_signal.signal.value = self.current_signal.signal.value * self.weight

        if self.branch.branch_dna.allowed_receptors == self.current_signal.nt_type: # If NT's match, the hand off to the connecting branch is attempted once


            if self.branch.mitochondrion.consume(self.current_signal.cost): # If Mitochondrion from Branch can afford receiving a signal it does


                if self.residual_charge is None: # If no residual charge exists, the signal is only passed on without further modulation
                    self.branch.current_signal = self.current_signal
                    self.current_signal = None

                else: # If residual charge exists and the mitochondrion can afford the transport, the signal is passed on with modulation and adding the residual charge.
                    self.current_signal.signal.value = lif_model(self.leak_factor,
                                                                 self.current_signal.signal.value,
                                                                 self.residual_charge)
                    self.branch.current_signal = self.current_signal
                    self.current_signal = None
                    self.residual_charge = None

            else:
                current_charge = self.current_signal.signal.value if self.current_signal.signal.value is not None else 0
                self.residual_charge = lif_model(self.leak_factor,
                                                 self.current_signal.signal.value,
                                                 current_charge)
                self.current_signal = None

        else: # NT's from Branch and Synapse do not match
            current_charge = self.current_signal.signal.value if self.current_signal.signal.value is not None else 0
            self.residual_charge = self.residual_charge if self.residual_charge is not None else 0
            self.residual_charge = lif_model(self.leak_factor,
                                             self.current_signal.signal.value,
                                             current_charge
                                             )
            self.current_signal = None

    def synapse_overcharged(self) -> bool:
        if self.residual_charge < SYNAPSE_OVERCHARGE_THRESHOLD:
            return True
        return False


