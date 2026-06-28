import numpy as np


def linear(x):
    return x


def ReLu(x):
    return max(0, x)

def Sigmoid(x):
    return 1 / (1 + np.exp(-x))

def TanH(x):
    return np.tanh(x)

def SoftMax(x):
    return np.exp(x) / np.sum(np.exp(x))

def LeakyReLU(x):
    return np.maximum(0.01 * x, x)

def ELU(x):
    return np.where(x > 0, x, np.exp(x) - 1)

def SELU(x):
    return np.where(x > 0, x, 0.5 * x)

def GELU(x):
    return 0.5 * x * (1 + np.tanh(np.sqrt(2 / np.pi) * (x + 0.044715 * np.power(x, 3))))

