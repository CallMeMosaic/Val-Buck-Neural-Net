"""
Regions are the superficial structure coordinating a network of neurons or a subregion.

Subregions:
Subregions can be used for different layers (for example an input layer firing


:author: CallMeMosaic
:since: 0.0.1
:version: 0.0.1
"""
from typing import Optional

from fundamentals.control.time import Time
from fundamentals.neuron import Neuron


class Region:

    def __init__(self,
                 subregions: Optional[list[Region]],
                 network: Optional[list[Neuron]],
                 name: Optional[str],
                 time: Time = Time(),
                 time_frame: int = 1,
                 is_input: Optional[bool] = False,
                 is_output: Optional[bool] = False
                 ):

        #TODO: ALL OPTIONALS NEED ALSO CHECK FOR NONE
        self.subregions = subregions
        if not isinstance(self.subregions, list):
            raise TypeError("Subregions must be of type List")

        if not isinstance(self.subregions[0], Region):
            raise TypeError("Subregions must be of type List[Region]")


        self.network = network
        if not isinstance(self.network, list):
            raise TypeError("Network must be of type List")

        if not isinstance(self.network[0], Neuron):
            raise TypeError("Network must be of type List[Neuron]")


        self.time = time
        if not isinstance(self.time, Time):
            raise TypeError("Time must be of type Time")


        self.time_frame = time_frame
        if not isinstance(self.time_frame, int):
            raise TypeError("Time frame must be of type int")



        self.is_input = is_input
        if not isinstance(self.is_input, bool):
            raise TypeError("is_input must be of type bool")

        self.is_output = is_output
        if not isinstance(self.is_output, bool):
            raise TypeError("is_input must be of type bool")

        self.name = name



    def run(self):
        while self.time.counter < self.time_frame:

            if isinstance(self.subregions, list):

                for i in range(len(self.subregions)):

                    if not isinstance(self.subregions[i], Region):
                         raise TypeError(f"Critical Error: Object at Index {i} is NOT a Region. System cannot proceed like this and will terminate!")

                    if self.subregions[i].is_input:
                        self.subregions[i]




            else:
                if isinstance(self.network, list):

                    for i in range(len(self.network)):

                        if not isinstance(self.network[i], Neuron):
                            raise TypeError(f"Critical Error: Object at Index {i} is NOT a Neuron. System cannot proceed like this and will terminate!")

                        self.network[i].process()



        self.time.counter += 1
