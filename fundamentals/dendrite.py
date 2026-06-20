from typing import List, Dict, Optional, Tuple
import numpy as np

from fundamentals.dendrite_branch import DendriteBranch
from fundamentals.transmitters import Transmitters


class Dendrite:
    def init(
            self,
            length: float = 1.0, # default value is 1.0
    ):
        if length <= 0:
            raise ValueError("Length must be greater than 0")
        self.length = length

        # Dynamic Properties necessary to keep track of dendrite branches and transmitters
        self.accepted_transmitters: List[Transmitters] = []
        self.branches: List[DendriteBranch] = []

        #TODO: ADD DENDRITE BRANCHES METHOD

        #TODO: REMOVE DENDRITE BRANCHES METHOD



