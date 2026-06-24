from enum import Enum
class Transmitters(Enum):

    """
    Represents a set of neurotransmitters.

    This class is an enumeration of different neurotransmitters within the
    nervous system. It provides a standardized way to reference biochemical
    transmitters used for neuron-to-neuron communication.

    :cvar GLUTAMATE: Represents glutamate, a major excitatory neurotransmitter.
    :vartype GLUTAMATE: str

    :cvar GABA: Represents gamma-aminobutyric acid (GABA), a major inhibitory
                neurotransmitter. Inhibits neuron activity by lowering the membrane potential.
    :vartype GABA: str

    :cvar DOPAMINE: Represents dopamine, a neurotransmitter associated with
                    reward and motivation systems.
    :vartype DOPAMINE: str

    :cvar SEROTONIN: Represents serotonin, a neurotransmitter related to mood
                     regulation.
    :vartype SEROTONIN: str

    :cvar NOREPINEPHRINE: Represents norepinephrine, a neurotransmitter linked
                          to arousal and alertness.
    :vartype NOREPINEPHRINE: str

    :cvar ACETYLCHOLINE: Represents acetylcholine, a neurotransmitter
                         associated with muscle activation and cognitive
                         functions.
    :vartype ACETYLCHOLINE: str

    :author: CallMeMosaic
    :since: 0.0.1
    :version: 0.0.1
    """
    GLUTAMATE = "Glutamate"
    GABA = "GABA"
    DOPAMINE = "Dopamine"
    SEROTONIN = "Serotonin"
    NOREPINEPHRINE = "Norepinephrine"
    ACETYLCHOLINE = "Acetylcholine"
