import math
from math import exp


def lif_model(
        leak_factor: float = 0.5,
        injected_current: float = -50.0,
        current_charge: float = -50.0
)-> float:
    """
    Compute the new membrane potential for a leaky integrate-and-fire (LIF) neuron model.

    This function calculates the updated voltage of a neuron by applying the
    LIF model equation. The LIF model simulates the decay of the membrane
    potential over time and adds new input to the system.

    :param time: Time elapsed since the last voltage update, in seconds.
    :type time: Float
    :param tau: Membrane time constant, in seconds. This defines the rate of
        exponential decay for the voltage.
    :type tau: Float
    :param new_input: External input or stimulus applied to the neuron.
    :type new_input: Float
    :param current_voltage: Current membrane potential of the neuron.
    :type current_voltage: Float
    :return: The updated membrane potential of the neuron.
    :rtype: Float

    :author: CallMeMosaic
    :since: 0.0.1
    :version: 0.0.1
    """

    #TODO: COMPLEXITY AND O-NOTATION
    #TODO: DOCSTRING EDIT

    return leak_factor * current_charge + injected_current