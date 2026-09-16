from dataclasses import dataclass


@dataclass
class Signal:

    def __init__(
            self,
            value: float

    ):

        if not isinstance(value, float) or value is None:
            raise ValueError("Value must be a float")

        if value <= 0:
            raise ValueError("Value cannot be zero or less")

        self.value = value