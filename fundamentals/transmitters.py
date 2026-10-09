from enum import Enum

class Transmitters(Enum):

    """
    An enum to ensure only valid Neuro Transmitters can be selected and handed off to methods/instances.
    Prevents invalid types from being created, which could halt the Networks productivity.


    :var GLUTAMATE: String: Value is the String "Glutamate". Excitatory Transmitter.
    :var GABA: String: Value is the String "Gaba". Inhibitory Transmitter.
    :var DOPAMINE: String: Value is the String "Dopamine". Reward related Transmitter.
    :var SEROTONIN: String: Value is the String "Serotonin". Mood Regulation.
    :var NOREPINEPHRINE: String: Value is the String "Norepinephrine".
    :var ACETYLCHOLINE: String: Value is the String "Acetylcholine"

    :author: CallMeMosaic
    :since: 0.0.1
    :version: 0.0.2

    Changelog:
    - 0.0.2: Improved Documentation.
    """
    GLUTAMATE = "Glutamate"
    GABA = "GABA"
    DOPAMINE = "Dopamine"
    SEROTONIN = "Serotonin"
    NOREPINEPHRINE = "Norepinephrine"
    ACETYLCHOLINE = "Acetylcholine"
