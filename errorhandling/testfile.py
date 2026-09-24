import fundamentals
from fundamentals import dendrite
from fundamentals.dendrite_branch import DendriteBranch

from fundamentals.maths.activation_functions import ReLu
from fundamentals.maths.decay_function import cable_function
from fundamentals.mitochondrion import Mitochondrion

from fundamentals.neuron_dna import NeuronDNA
from fundamentals.transmitters import Transmitters

from fundamentals.control.time import Time


GTime = Time()
#print(cable_function(-0.75,-0.45,-0.45,0.234,1.1,1.3,0.1))

Dendrite = fundamentals.dendrite.Dendrite(Mitochondrion(),
                                          -52,
                                          -70,
                                          [DendriteBranch(None, Mitochondrion(), Transmitters.GABA, NeuronDNA(Transmitters.GABA, Transmitters.GABA, 22, GTime), 5, 2, 1.3)],
                                          GTime,
                                          5,
                                          5,
                                          22000

                                          )

print(round(Dendrite.leak_factor,10))
print(Dendrite.tau_membrane)
