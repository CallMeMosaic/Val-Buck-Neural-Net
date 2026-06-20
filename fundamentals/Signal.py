from dataclasses import dataclass


@dataclass
class Signal:

    def __init__(
            self,
            value: float

    ):
        self.value = value