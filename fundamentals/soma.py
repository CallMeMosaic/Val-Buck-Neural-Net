from numbers import Number
from typing import Optional, Tuple

from numpy.f2py.symbolic import Op

from fundamentals.Signal import Signal
from fundamentals.axon import Axon
from fundamentals.dendrite import Dendrite
from fundamentals.dendrite_branch import DendriteBranch
from fundamentals.maths.decay_function import cable_function
from fundamentals.mitochondrion import Mitochondrion
from fundamentals.nucleus import Nucleus
from fundamentals.transmitters import Transmitters
from fundamentals.transmitters_cost import TransmittersCost

#TODO: Needs threshold

class Soma:
    """
    Represents the Soma, the cell body of a neuron, responsible for integration and processing of
    incoming signals. It interfaces with dendrites, an axon, a mitochondrion for energy supply,
    and a nucleus for genetic material. Soma processes signals and generates outgoing signals
    when needed, considering its threshold and refractory state.

    :ivar axon: The axon is connected to the Soma, responsible for transmitting outgoing signals.
    :type axon: Axon
    :ivar dendrites: A list of dendrites connected to the Soma, responsible for receiving incoming signals.
    :type dendrites: list[Dendrite]
    :ivar name: Optional name of the Soma to distinguish it, if required.
    :type name: Optional[str]
    :ivar mitochondrion: The mitochondrion supplying energy for the Soma's operations.
    :type mitochondrion: Mitochondrion
    :ivar nucleus: The nucleus containing genetic material and regulating Soma functions.
    :type nucleus: Nucleus
    :ivar threshold: The minimum energy threshold needed to process an incoming signal.
    :type threshold: Float
    :ivar refractory_period: Period during which the Soma cannot fire another signal after processing one.
    :type refractory_period: Float
    :ivar is_exhausted: A boolean flag indicating whether the Soma is in an exhausted state, unable to process signals.
    :type is_exhausted: Bool
    :ivar refractory_timer: Tracks the remaining time in the Soma's refractory period.
    :type refractory_timer: Int
    :ivar fired_stat: Tracks whether the Soma has fired a signal in the current time step. Gets reset after one timestep and is needed for the layer-control/region to track firing sequences.
    :type fired_stat: Bool

    :author: CallMeMosaic
    :since: 0.0.1
    :version: 0.0.1
    """

    def __init__(self,
                 nucleus: Nucleus, # The Cells Nucleus, containing the DNA of the cell and housing (FUTURE UPDATE) methods to manage the cells' DNA
                 mitochondrion:Mitochondrion, # The Cells Mitochondrion, necessary for energy management of the soma.
                 axon: Axon, # The axon connected to the soma, necessary for delivering signals to other neurons.
                 dendrites: list[Dendrite], # A list of all dendrites connected to the soma, necessary for receiving signals from other neurons.
                 baseline_charge: float = -50.0, # mV This is the resting potential of the Soma, the charge paramter will always be reset to this value after firing.
                 threshold: float = -50.0, # mV This is the action potential threshold of the Soma, if the charge exceeds/meets this value, the Soma will fire.
                 refractory_period: int = 5, # The refractory period of the Soma, the time it takes for the Soma to recover from firing.
                 fired_stat: bool = False, # A boolean indicating whether the Soma has fired in the previous timestep, gets reset after the refractory period is over.
                 name: Optional[str] = None
                 ):

        # Ensure Typing for Nucleus is according to the type hints

        if not isinstance(nucleus, Nucleus) or nucleus is None:
            raise TypeError("Nucleus must be instance of class Nucleus")

        self.nucleus = nucleus


        # Ensure Typing for Mitochondrion is according to the type hints

        if not isinstance(mitochondrion, Mitochondrion) or mitochondrion is None:
            raise TypeError("Mitochondrion must be instance of class Mitochondrion")

        self.mitochondrion = mitochondrion

        # Ensure Typing for Axon is according to the type hints

        if not isinstance(axon, Axon) or axon is None:
            raise TypeError("Axon must be instance of class Axon")

        self.axon = axon

        # Ensure Typing for Dendrites is according to the type hints

        if not isinstance(dendrites, list) or dendrites is None:
            raise TypeError("Dendrites must be instance of class list")

        for dendrite in dendrites:
            if not isinstance(dendrite, Dendrite) or dendrite is None:
                raise TypeError("Dendrite objects within Dendrites must be instance of class Dendrite")

        self.dendrites = dendrites


        # Ensure Typing for Baseline Charge is according to the type hints

        if baseline_charge is not None:

            if not isinstance(baseline_charge, Number) or isinstance(baseline_charge, bool):
                raise TypeError("Baseline charge must be instance of class Number and not bool")

            else:

                if baseline_charge > 0:
                    raise ValueError("Baseline charge must be below 0")

                baseline_charge = float(baseline_charge)

        else:
            raise TypeError("Baseline charge cannot be None")

        self.baseline_charge = baseline_charge


        # Ensure Typing for Threshold is according to the type hints

        if threshold is not None:

            if not isinstance(threshold, Number) or isinstance(threshold, bool):
                raise TypeError("Threshold must be instance of class Number and not bool")

            else:

                if threshold > 0:
                    raise ValueError("Threshold must be greater than 0")

                threshold = float(threshold)

        else:
            raise TypeError("Threshold cannot be None")

        self.threshold = threshold


        # Ensure the Refractory Period is according to the type hints

        if refractory_period is not None:

            if not isinstance(refractory_period, Number) or isinstance(refractory_period, bool):
                raise TypeError("Refractory Period must be instance of class Number and not bool")

            else:

                if refractory_period <= 0:
                    raise ValueError("Refractory Period must be greater than 0")

                refractory_period = int(refractory_period)

        else:
            raise TypeError("Refractory Period cannot be None")

        self.refractory_period = refractory_period


        # Ensure the Fired Stat is according to the type hints

        if not isinstance(fired_stat, bool) or fired_stat is None:
            raise TypeError("Fired Stat must be instance of class bool and not None")

        self.fired_stat = fired_stat

        # TEMP THING FOR NAME
        self.name = name



    def branch_process(self, branch: DendriteBranch, dendrite: Dendrite):
        """
        Applies the cable function to all the dendrite branches and updates the dendrite charge
        per branch.
        Needs to be passed the Dendrite object to process, it's specific sub-branches.
        Also ensures the Signal object is deleted after being used for transmitting the charge.

        :param dendrite = Dendrite: The dendrite object to process.
        :param branch = DendriteBranch: The branch object to process.


        CONSUMPTION:
        FLOPS = 10
        Logic Instructions = 4

        :return:
        """

        # Step 0: Check if the Mitochondrion of the Branch can handle the current action and if there is a signal to process
        if not branch.mitochondrion.consume(TransmittersCost.TRANSPORT_INTERNALLY):
            return

        if branch.current_signal is None: # Ensures branches are only processed if there is a signal to process to save computation
            return

        # Step 1: Remove value from a signal object and remove reference for GC
        injected_charge = branch.current_signal.value
        branch.current_signal = None


            # Step 2: Simulate the way from dendrite branch to dendrite
            dendrite.charge = cable_function(None,
                                            injected_charge,
                                            dendrite.charge,
                                            branch.space_constant,
                                            branch.membrane_resistance,
                                            branch.attenuation_factor,
                                            branch.time_scaling_factor,)




    def dendrite_process(self,dendrite: Dendrite):

        for branch in dendrite.branches:

            self.branch_process(branch,dendrite)
            # Checks branch, if no signal at branch, nothing happens
            # If branch mitochodrium cannot accomodate the internal transport of a charge, nothing happens


        # Calculate the charge that all the branches have injected into the dendrite

        if not dendrite_prior_charge == dendrite.charge:
            dendrite_injected_charge = dendrite_prior_charge - dendrite.charge


        # Apply leaky function before firing, so that it is always applied and can possibly prevent a fire
        dendrite.charge = lif_model(dendrite.leak_factor,
                                    dendrite.injected_charge,
                                    dendrite_prior_charge)

        # Check if the dendrite has reached its local threshold
        if dendrite.charge >= dendrite.local_threshold:

            # Validate that can be fired
            if dendrite.mitochondrion.consume(TransmittersCost.FIRE):

                # Run the cable function to pass the charge from the dendrite to the soma
                self.current_charge = cable_function(dendrite.charge,
                                                    dendrite.baseline_charge,
                                                    self.current_charge,
                                                    dendrite.space_constant,
                                                    dendrite.membrane_resistance,
                                                    dendrite.attenuation_factor,
                                                    dendrite.time_scaling_factor)



            if dendrite.charge > dendrite.local_threshold:
                cable_function(dendrite.charge, dendrite.baseline_charge, self.)



    def process(self, incoming: float) -> Signal | None:
        # TODO: - Implement this
        # TODO: Should use the data contained in the NeuroTransmitter and process it
        # TODO: RUN CHECK UP ON MITOCHONDRION
        # TODO: ADD CABLE THEORY
        # TODO: NEEDS TO CHECK MEMBRANE CHARGE AND THRESHOLD TO FIRE

        if not self.mitochondrion.consume():
            self.is_exhausted = True
            return None

        if self.refractory_timer > 0:
            self.refractory_timer -= 1
            # Still do the maths, but don't fire
            return None

        else:
            if self.mitochondrion.consume(TransmittersCost.STANDARD):
                # DO Maths here
                outgoing = Signal(2)  # PLACEHOLDER
                return outgoing
            else:
                # Save the signal for later?
                return None

    def assign_transmitter(self, signal: Signal) -> Tuple[Transmitters, TransmittersCost]:
        # TODO: - Implement this
        # TODO: Should use the Signal returned from the process method to assign a transmitter and return said transmitter
        # TODO: RETURN TYPE IS CROOKED
        # TODO: RUN CHECK UP ON MITOCHONDRION

        self.mitochondrion.consume(TransmittersCost.STANDARD)
        transmitter_tuple: Tuple
        return transmitter_tuple[Transmitters, TransmittersCost]


    def fire(self):
        self.mitochondrion.consume(TransmittersCost.FIRE)
        # TODO: -implement this
        # TODO: Should command the firing of the transmitter
        pass
