from math import exp


def spatial_decay(voltage: float, distance: float, length_delta: float = 1.0) -> float:
    """
    Calculate the spatial decay of a signal over a given distance.

    This function computes the decay of a signal based on its initial voltage,
    the distance it travels, and an optional length constant delta. The length
    constant delta determines the rate of decay.

    :param voltage: Initial voltage of the signal before decay.
    :type voltage: Float
    :param distance: Distance over which the signal decays.
    :type distance: Float
    :param length_delta: Optional length constant that affects the rate of
        decay. Defaults to 1.0.
    :type length_delta: float
    :return: The decayed voltage of the signal after traveling the specified
        distance.
    :rtype: Float

    :author: CallMeMosaic
    :since: 0.0.1
    :version: 0.0.1

    """

    return(
        voltage * exp(-distance/length_delta)
    )