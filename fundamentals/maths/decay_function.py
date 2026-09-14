def length_constant():




def leaky_function(

):

    return x


def cable_function(
    injected_current: float=0.1,
    membrane_resistance: float=100.0,
    lambda: float=0.01,

):
    """

    :param injected_current: The current injected into the soma/dendrite will be added onto the pre-existing current.
    :param membrane_resistance: Represents the membrane resistance per unit length. Higher resistance values lead to less current loss over distance.
    :param lambda: The length constant, governing the general spatial decay.
    :return:
    """


    return x