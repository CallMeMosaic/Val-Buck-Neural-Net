from typing import Any


class NotEnoughCharge(Exception):
    pass

class NeuronError(Exception):
    pass

class NeuronDNAError(NeuronError):
    """Raised when there is a mismatch between DNA data and actual data"""

    def __init__(self, module:Any, expected:Any, actual:Any):
        module = module
        expected = expected
        actual = actual
        super().__init__(f"DNA mismatch: {module.__name__} expects: {expected.__name__}, but got: {actual.__name__}")
