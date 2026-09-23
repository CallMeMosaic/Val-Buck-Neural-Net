import math

from math import sqrt
from typing import Optional


def length_constant():
    pass


"""
def leaky_function(

):

    return x
"""

def cable_function(
    injected_current: Optional[float] = None,
    prior_charge: float= 0.0,
    following_charge: float=0.0,
    space_constant: float=1.0,
    membrane_resistance: float=1.0,
    attenuation_factor: float=1.0,
    time_scaling_factor: float=1.0,


):
    """
    FUNCTION HAS TO BE EXECUTED AT THE RECEIVING END OF THE CABLE

    :param injected_current:
    :param prior_charge:
    :param following_charge:
    :param space_constant:
    :param membrane_capacitance:
    :param attenuation_factor:
    :param time_scaling_factor:

    :return = float: the new charge of the succeeding end of the cable.
    """
    if injected_current is not None:
        current_charge = (membrane_resistance * injected_current) / (2 * space_constant) # FLOPS: 4
        input_charge = current_charge + prior_charge # FLOPS: 1
    else:
        input_charge = prior_charge # FLOPS: 1


    return following_charge + ( input_charge * attenuation_factor -  following_charge ) * time_scaling_factor # FLOPS: 4
