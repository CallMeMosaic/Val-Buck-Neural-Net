from dataclasses import dataclass


@dataclass
class Signal:

    def __init__(
            self,
            value: float

    ):
        if value is not None:
            self.value = value
        else:
            raise ValueError("Value cannot be None")