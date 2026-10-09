![Header Image](assets/preview.webp)

# Spark-V2 (Val-Buck-Neural-Net)

Spark-V2 is a biologically-inspired neural network framework that models the complex interactions of biological neurons. Unlike traditional artificial neural networks that use simplified mathematical abstractions, Spark-V2 incorporates concepts such as neurotransmitters, mitochondrial energy management, and DNA-constrained cellular functions.

## 🧠 Core Philosophy

The project aims to provide a granular simulation of neural activity, where each "Neuron" is a complex entity composed of several specialized biological structures. This allows for modeling not just signal propagation, but also the metabolic costs and chemical constraints associated with biological intelligence.

Unlike traditional ANNs that rely on static weights and backpropagation, Spark-V2 is designed as a dynamic, "living" system where intelligence emerges from the complex interplay of biological constraints and chemical signaling.

## 🎯 Target Use Case

Spark-V2 is currently being developed as the foundational neural architecture for a broader **AGI (Artificial General Intelligence) Project**. It serves as the underlying layer for various neural networks within that system, providing a more robust and biologically plausible substrate for artificial thought.

## 🚀 Future Concept & Vision

The long-term vision for Spark-V2 includes:

- **Beyond Backpropagation**: Moving towards a purely dynamic system where learning and adaptation occur naturally through biological mechanisms rather than mathematical optimization alone.
- **Multi-purpose Networks**: Developing networks that can serve multiple functional roles simultaneously by utilizing different Neurotransmitters, mimicking the versatility of the human brain.
- **Emergent Complexity**: Leveraging the interaction between energy constraints (`Mitochondrion`) and genetic blueprints (`NeuronDNA`) to foster emergent behaviors in complex neural architectures.

## ✨ Key Features

- **Biological Accuracy**: Models components like Axons, Dendrites, Somas, and Nuclei.
- **Energy Management**: Includes `Mitochondrion` objects that track energy capacity and recharge rates, influencing a neuron's ability to function.
- **Chemical Signaling**: Uses various `Transmitters` (Glutamate, GABA, Dopamine, Serotonin, etc.) for communication between units.
- **Genetic Constraints**: `NeuronDNA` defines what a specific neuron can synthesize or receive.
- **Metabolic Cost**: Synthesizing neurotransmitters and processing signals has an energy cost (`TransmittersCost`).

## 🛠️ Requirements

- **Python**: 3.14 or higher
- **Dependencies**: `numpy` (>= 2.4.6)

## 🚀 Installation

This project uses `uv` for dependency management.

```bash
# Clone the repository
git clone https://github.com/yourusername/Val-Buck-Neural-Net.git
cd Val-Buck-Neural-Net

# Install dependencies
uv sync
```

## 🏗️ Project Structure

The core logic is located in the `fundamentals/` directory:

- `neuron.py`: The main container for neural components.
- `axon.py`: Handles neurotransmitter synthesis and signal output.
- `soma.py`: The cell body where signal processing occurs.
- `nucleus.py`: Contains the DNA and dictates cellular capabilities.
- `mitochondrion.py`: Manages the energy (ATP equivalent) of the cell.
- `neuro_transmitter.py`: Defines the chemical messages sent between neurons.
- `transmitters.py`: Enumeration of supported neurotransmitters (Glutamate, GABA, etc.).
- `neuron_dna.py`: Defines the genetic blueprint of allowed receptors and syntheses.

## 📖 Usage Example

```python
from fundamentals.nucleus import Nucleus
from fundamentals.neuron_dna import NeuronDNA
from fundamentals.mitochondrion import Mitochondrion
from fundamentals.transmitters import Transmitters
from fundamentals.axon import Axon

# Define what this neuron can do
dna = NeuronDNA(
    allowed_receptors=(Transmitters.GLUTAMATE,),
    allowed_syntheses=(Transmitters.DOPAMINE,)
)

# Create cellular components
nucleus = Nucleus(dna=dna)
powerhouse = Mitochondrion(capacity=100.0, efficiency_lambda=0.8)

# Initialize an Axon
axon = Axon(nucleus=nucleus, mitochondrion=powerhouse)

# Now the neuron can synthesize neurotransmitters if it has enough energy!
```

## 🤝 Contributing

If you'd like to contribute to this project, go ahead and contact me, as this project is currently not licenses at all.
Although feedback is always appreciated.

## 📜 Authors & Acknowledgments

- **Lead Developer**: CallMeMosaic
- **Project Name**: Spark-V2 (originally Val-Buck-Neural-Net)
