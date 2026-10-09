import math
from numbers import Number

from fundamentals.axon_terminal import AxonTerminal
from fundamentals.dendrite_branch import DendriteBranch
from fundamentals.maths.CONSTANTS import SYNAPSE_TAU_MEMBRANE, DELTA_T, SYNAPSE_OVERCHARGE_THRESHOLD
from fundamentals.maths.lif_model import lif_model
from fundamentals.synaptic_membrane import SynapticMembrane

#TODO: SUCCESSFUL TRANMISSION NEEDS TO STRENGTHEN THE SYNAPSE. AKA LOWER MEMBRANE RESISTANCE.


class Synapse:
    """
    The synapse object links an axon_terminal and a dendrite_branch.
    The axon terminal acts as an input, passing a newly synthesized NeuroTransmitter object on, which is saved as the
    current_signal property. The only task the synapse does is applying it's weight to the incoming charge and
    either handing the signal on to the dendrite_branch or storing it
    in a queue, which then applies the leak function and adds it to the residual charge parameter.


    :param weight: Float: The Synaptic weight applied to the charge carried by the NeuroTransmitter before handoff. A float between 0.1 and 10
    :param membrane: SynapticMembrane: REDUNDANT
    :param terminal: AxonTerminal: The transmitting end of the synapse (Input)
    :param branch: DendriteBranch: The receiving end of the synapse (output)


    Late-Initialized Properties:
    :property current_signal: The currently processed signal. Not a parameter as none needs to be present for creation of a synapse

    :author: CallMeMosaic
    :since: 0.0.1
    :version: 0.0.2

    Changelog:
    - 0.0.2: Improved Documentation.

    """


    def __init__(
            self,
            weight: float,
            membrane: SynapticMembrane,
            terminal: AxonTerminal,
            branch: DendriteBranch
    ):

        # Ensure weight is according to type hints

        if weight is not None:

            if isinstance(weight, Number) and not isinstance(weight, bool):

                if weight >= 0 and weight <= 10:

                    self.weight = float(weight)

                else:
                    raise ValueError("Weight of synapse needs to be more than 0 and in reasonable modulation range.")

            else:
                raise TypeError("Weight needs to be instance of class Number and cannot be Boolean!")

        else:
            raise TypeError("Weight cannot be None!")


        # Ensure membrane is according to type hint

        if membrane is not None:

            if isinstance(membrane, SynapticMembrane):

                self.membrane = membrane

            else:
                raise TypeError("Synaptic Membrane needs to be instance of class SynapticMembrane")

        else:
            raise TypeError("Synaptic Membrane cannot be None")


        # Ensure terminal is according to type hint

        if terminal is not None:

            if isinstance(terminal, AxonTerminal):

                self.terminal = terminal

            else:
                raise TypeError("Axon Terminal must be instance of class AxonTerminal")

        else:
            raise TypeError("Axon Terminal cannot be none")


        # Ensure branch is according to type hints

        if branch is not None:

            if isinstance(branch, DendriteBranch):

                self.branch = branch

            else:
                raise TypeError("Branch needs to be instance of class DendriteBranch")

        else:
            raise TypeError("Branch cannot be None")

        # Late initialized and math properties

        self.current_signal = None

        self.leak_factor = 1 / weight # Inverses the weight to keep modulation for leak

        self.residual_charge = 0

        self.leak_factor = math.exp(-DELTA_T / SYNAPSE_TAU_MEMBRANE)


    """
    ————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
    """


    def calculate_and_strip(self):
        """
        Calculates the amount of charge which will be handed off to the connected dendrite branch.
        If the mitochondrion can afford the transfer and the neurotransmitters match, the hand off will be attempted.
        The method will also check if a residual charge exists, if so it will apply the lif model and then pass on the modulated charge.
        If no residual charge is detected it will just pass the charge on by setting the dendrite branche's current sinal property to it's charge.
        If hand off is refused for any reason, the charge will be added to the residual charge property and lif model will be applied.
        Deletes all references to the Neuro Transmitter object and only hands off the signal object.


        :author: CallMeMosaic
        :since: 0.0.1
        :version: 0.0.2

        Changelog:
        - 0.0.2: Improved Documentation.

        """

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


    """
    ————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
    """


    def synapse_overcharged(self) -> bool:
        """
        Metod to detect if the Synapse hand off has been refused too many times.
        Used in the Neuron's tick method to detect if a connection is viable.
        If this method returns true, the Synapse will be deleted.


        :author: CallMeMosaic
        :since: 0.0.1
        :version: 0.0.2

        Changelog:
        - 0.0.2: Improved Documentation.

        """
        if self.residual_charge < SYNAPSE_OVERCHARGE_THRESHOLD:
            return True
        return False


