

class Time:

    """
This module provides a Time class for tracking time. This is neceassary to enable temporal factors in the SNN and to
even make it calssify as an SNN.
The time calss is supposed to be a global time ticker.

:author: CallMeMosaic
:since: 0.0.1
:version: 0.0.1
    """


    def __init__(self):
        self.counter = 0

    def tick(self):
        self.counter += 1

    def reset(self):
        self.counter = 0


#class GodTime: