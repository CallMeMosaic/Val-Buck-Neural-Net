from numbers import Number
from typing import Optional

import math
from math import sqrt

from errorhandling.neuron_exceptions import NeuronDNAError
from fundamentals.Signal import Signal
from fundamentals.maths.CONSTANTS import DELTA_T
from fundamentals.mitochondrion import Mitochondrion
from fundamentals.neuron_dna import NeuronDNA
from fundamentals.transmitters import Transmitters


class DendriteBranch:
    """
    Dendrite Branch class. Provides Properties necessary for spatial decay calculation
    and Neuro Transmitter propagation. Gets handed a signal Object by its preceding
    Synapse. Strips the carried charge of it's Signal object and removes references to the Signal object for GC to collect it.

    :param current_signal: Signal:
    :param mitochondrion: Mitochondrion:
    :param receptor_type: Transmitters:
    :param branch_dna: NeuronDNA:
    :param length: Int:
    :param width: Int:
    :param membrane_resistance: Float:

    Late-Initialized Properties:
    :property internal_resistance: Float: Internal resistance of the axon to charge dissipating.
    :property space_constant: Float: The square root of the membrane resistance divided by the axon's internal resistance. Indicates how much percentage of charge dissipates over one length unit.
    :property cable_area: Float: The surface area of the axon. It is calculated as the product of the axon's width and length.
    :property membrane_capacitance: Float: How much the membrane stores/absorbs charge over the length of the axon.
    :property tau_membrane: Float: The time constant of the membrane, calculated as the product of the membrane resistance and membrane capacitance.
    :property attenuation_factor: Float:
    :property time_scaling_factor: Float:

    :author: CallMeMosaic
    :since: 0.0.1
    :version: 0.0.3

    Changelog:
        - 0.0.2: Added proper type hints and removed unnecessary stuff
                 Also added parameter for dna of soma, so no branch can be built that would accept invalid signals (neuron cancer? I mean biologically it is possible probably???)
                 Added width parameter for spatial decay calculation.
                 Added Mitochondrion parameter for energy consumption.

        - 0.0.3: Changed Documentation and optimized readability.
    """

    # TODO: ADD LINKED SYNAPSE!!! No
    def __init__(
            self,
            current_signal: Signal | None,
            mitochondrion: Mitochondrion,  # The Powerhouse of each cell innit
            receptor_type: Transmitters,  # From transmitters enum
            branch_dna: NeuronDNA,
            # Ensures that the Branches cannot receive signals from neurons that use different Neuro Transmitters
            length: int = 1,  # default value is 1.0, needed for spatial decay calculation
            width: int = 1,  # default value is 1.0, needed for spatial decay calculation
            membrane_resistance: float = 1.0,
            name: Optional[str] = None,  # Optional name for easier debugging
    ):
        # Ensure the current Signal follows type hints, Can be None as it is set to none when signal is processed

        if current_signal is not None and not isinstance(current_signal, Signal):
            raise TypeError("current_signal must instance of class Signal")

        self.current_signal = current_signal



        # Ensure the DNA passes type hints
        if not isinstance(branch_dna, NeuronDNA) or branch_dna is None:
            raise TypeError("branch_dna must instance of class NeuronDNA")

        self.branch_dna = branch_dna


        # Ensure Mitochondrion passes type hints

        if not isinstance(mitochondrion, Mitochondrion) or mitochondrion is None:
            raise TypeError("mitochondrion must instance of class Mitochondrion")

        self.mitochondrion = mitochondrion



        # Ensure the current receptor type matches the DNA
        if not isinstance(receptor_type, Transmitters) or receptor_type is None:
            raise TypeError("receptor_type must instance of class Transmitters")

        if branch_dna.allowed_receptors != receptor_type:
            raise NeuronDNAError(module=self, expected=branch_dna.allowed_receptors, actual=receptor_type)

        self.receptor_type = receptor_type


        # Ensure length passes a type hint and is reasonable

        if not isinstance(length, Number) or isinstance(length, bool):
            raise TypeError("Length must be a number")
        else:
            length = int(length)

        if length <= 0:
            raise ValueError("Length must be greater than 0")

        self.length = length


        # Ensure width passes the type hint and is reasonable

        if not isinstance(width, Number) or isinstance(width, bool):
            raise TypeError("Width must be a number")
        else:
            width = int(width)

        if width <= 0:
            raise ValueError("Width must be greater than 0")

        self.width = width


        # Ensure membrane_resistance passes type hints

        if not isinstance(membrane_resistance, Number) or isinstance(membrane_resistance, bool):
            raise TypeError("Membrane resistance must be a number")
        else:
            membrane_resistance = float(membrane_resistance)

        self.membrane_resistance = membrane_resistance


        # Values for cable theory DO THIS WITH DNA LATER

        self.internal_resistance = 10 / width

        self.space_constant = sqrt(membrane_resistance / self.internal_resistance)

        self.cable_area = width * length * math.pi

        self.membrane_capacitance = 1.0 * self.cable_area

        self.tau_membrane = self.membrane_capacitance * membrane_resistance

        self.attenuation_factor = math.exp(-length / self.space_constant)

        self.time_scaling_factor = (DELTA_T / self.tau_membrane)
