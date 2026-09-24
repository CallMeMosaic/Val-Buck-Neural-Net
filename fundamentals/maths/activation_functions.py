import abc
from abc import ABC

import numpy as np

class ActivationFunction(ABC) :
    @abc.abstractmethod
    def calculate(self,x: float) -> float:
        """Subclass should have the actual function here"""


class Linear(ActivationFunction):
    def calculate(self,x: float) -> float:
        return x


class ReLu(ActivationFunction):
    def calculate(self,x: float) -> float:
        return max(0, x)


class Sigmoid(ActivationFunction):
    def calculate(self,x: float) -> float:
        return 1 / (1 + np.exp(-x))


class TanH(ActivationFunction):
    def calculate(self,x: float) -> float:
        return np.tanh(x)

class SoftMax(ActivationFunction):
    def calculate(self,x: float) -> float:
        return np.exp(x) / np.sum(np.exp(x))

class LeakyReLU(ActivationFunction):
    def calculate(self,x: float) -> float:
        return np.maximum(0.01 * x, x)

class ELU(ActivationFunction):
    def calculate(self,x: float) -> float:
        return np.where(x > 0, x, np.exp(x) - 1)

class SELU(ActivationFunction):
    def calculate(self,x: float) -> float:
        return np.where(x > 0, x, 0.5 * x)

class GELU(ActivationFunction):
    def calculate(self,x: float) -> float:
        return 0.5 * x * (1 + np.tanh(np.sqrt(2 / np.pi) * (x + 0.044715 * np.power(x, 3))))

