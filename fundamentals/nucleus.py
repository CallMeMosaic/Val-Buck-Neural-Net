from typing import Callable, List, Union
from fundamentals.mitochondrion import Mitochondrion
from fundamentals.neuro_transmitter import NeuroTransmitter
from fundamentals.neuron_dna import NeuronDNA
from fundamentals.transmitters import Transmitters

#TODO: - Add Activation Function in here


class Nucleus:
    """
    Represents the nucleus of a neuron.

    This class is responsible for handling the synthesis and reception of
    neurotransmitters within a neuron. It utilizes the DNA information
    provided to determine what neurotransmitters can be synthesized and
    received.

    :ivar dna: Represents the NeuronDNA, which provides constraints on what
        neurotransmitters the neuron can synthesize or receive.
    :type dna: NeuronDNA

    :author: CallMeMosaic
    :since: 0.0.1
    :version: 0.0.1
    """
    def __init__(
            self,
            dna: NeuronDNA, # Neccessary for the neuron to know what it can synthesize and receive

    ):
        # Check if the dna is not None
        if dna is None:
            raise ValueError("DNA CANNOT BE NONE! NEURON CREATION FAILED")
        self.dna = dna

    def activation_function(self, lambda_function: Callable,):
        pass






