from typing import List


class ConversionFunctions:

    def MNISTToST(
            self,
            input=List,
            frequency=bool
    ):
        converted = []
        if frequency:
            for i in range(len(input)):
                converted.append((input[i]/256)*100) # returns frequency in spike trains per 100 time steps
        else:
            for i in range(len(input)):
                converted.append((input[i]/256)) # returns a probability for a neuron to spike per timestep
        return converted