
from typing import Optional, List

from fundamentals.control.time import Time
from fundamentals.neuron import Neuron


class Region:

    """
Regions are the superficial structure coordinating a network of neurons or a subregion.

Subregions:
Subregions can be used for different layers (for example an input layer firing)


:author: CallMeMosaic
:since: 0.0.1
:version: 0.0.1
"""

    def __init__(self,
                 subregions: Optional[list[Region]],
                 network: Optional[list[Neuron]],
                 name: Optional[str],
                 time: Time = Time(),
                 time_frame: int = 100,
                 is_input: Optional[bool] = False,
                 is_output: Optional[bool] = False
                 ):

        #TODO: ALL OPTIONALS NEED ALSO CHECK FOR NONE

        if subregions is not None: # Type checks for optional parameter subregions. Checks if it exists and then if it is a list and if each element is an instance of Region.
            if not isinstance(subregions, list):
                raise TypeError("Subregions must be of type List")
            for sr in subregions:
                if not isinstance(sr, Region):
                    raise TypeError("Subregions must be of type List[Region]")
        self.subregions = subregions


        if network is not None: # Type checks for optional parameter network. Checks if it exists and then if it is a list and if each element is an instance of Neuron.
            if not isinstance(network,list):
                raise TypeError("Network List must be of type List")
            for n in network:
                if not isinstance(n, Neuron):
                    raise TypeError("Network List must be of type List[Neuron]")
        self.network = network


        if not isinstance(time, Time): #Type check for parameter time to ensure it was set correctly.
            raise TypeError("Time must be of type Time")
        self.time = time


        if not isinstance(time_frame, int): # Type check for parameter time_frame to ensure it was set correctly.
            raise TypeError("Time frame must be of type int")
        self.time_frame = time_frame


        if is_input is not None: # Type check for optional parameter is_input. Checks if it exists and then if it is a boolean.
            if not isinstance(is_input, bool):
                raise TypeError("is_input must be of type bool")
        self.is_input = is_input



        if not isinstance(is_output, bool): # Type check for optional parameter is_output. Checks if it exists and then if it is a boolean.
            raise TypeError("is_input must be of type bool")
        self.is_output = is_output


        if name is not None:
            self.name = name

    def run(self,input=None):


        while self.time.counter < self.time_frame:
            self.step(input=input)
            self.time.counter += 1
        # possible return of output?


    def step(self,input:List=None):
        """
        Function that runs the entire region's neural network and/or it's subregions within a given timeframe.
        Within each time step the run function will call the process functions of all neurons within its neural network list.
        In case the region is a super region, containing subregions with their own respective subregions or neural networks, the run function
        calls the subregion's run functions.
        The function also detects whether its assigned neural network is supposed to be an input, output, or standard layer.
        If it detects that it is an input layer region, it will call the process function of each neuron with the pre-converted input data.
        If it detects that it is an output layer region, it will call the process function of each neuron and append its return value to an output list, which
        it then returns.
        The function runs until the time frame is reached and then checks if output data exists, if that is the case, it returns it.

        @Deprecated :param conversion_method:
        :param input: An optional parameter that should contain the pre-converted input data (converted to either spike frequency or spike chance).
        :return: output: An optional return value that contains the spike counts of each output neuron. Gets updated per recursion and returned at the end of the function.

        @author: CallMeMosaic
        @since: 0.0.1
        @version: 0.0.1
        """

        output = [] # Needed at top level so the output list can be accessed and updated inside the while loop and returned outside it.

        if input is not None: # Type check for optional parameter input. Checks if it exists and then if it is a list.

            if not isinstance(input,List):
                raise TypeError("Input must be of type List")

            #input = conversion_method(input,True) # Deprecated, will be moved into a separate algorithm outside the region

            #TODO: FIX THE LOOPING THEN YOU'RE DONE!

        while self.time.counter < self.time_frame: # Loop through the time frame. For time simulation

            if isinstance(self.subregions, list) and self.subregions is not None: # Type check for optional parameter subregions. Make sure it is a list.

                for i in range(len(self.subregions)): # Iterate through each element of the subregion.

                    if not isinstance(self.subregions[i], Region): # Check that each element is of type Region.
                         raise TypeError(f"Critical Error: Object at Index {i} is NOT a Region. System cannot proceed like this and will terminate!")

                    if self.subregions[i].is_input: # Check if the current subregion is an input region. If so, call its run function with the input parameter.
                        self.subregions[i].run(input) # input param hands the list of converted input values down to subregion.

                    elif self.subregions[i].is_output: # Check if the current subregion is an output region.
                        self.subregions[i].run()

                    else: # If the current subregion is neither an input nor an output region, call its run function without any parameters.
                        self.subregions[i].run()




            else: # If Region does not have any subregions call each neuron in the network.

                if isinstance(self.network, list) and self.network is not None: # Type check to make sure network exists and is a list.

                    if self.is_input: # Check if the region itself is an input region.


                        for i in range(len(self.network)): # Run through each input neuron.

                            if not isinstance(self.network[i], Neuron) or self.network[i] is None: # Type check to make sure neuron exists and is a Neuron.
                                raise TypeError(f"Critical Error: Object at Index {i} is NOT a Neuron. System cannot proceed like this and will terminate!")

                            if input[i] is None: # Type check to make sure input exists and is not None.
                                raise TypeError(f"Critical Error: Input at Index {i} is None. System cannot proceed like this and will terminate!")


                            self.network[i].process(input[i]) # Call each neuron's process function with the input parameter

                    elif self.is_output: # Check if the region itself is an output region.


                        for i in range(len(self.network)): # Iterate through each neuron.

                            if not isinstance(self.network[i], Neuron) or self.network[i] is None: # Type check to make sure neuron exists and is a Neuron.
                                raise TypeError(f"Critical Error: Object at Index {i} is NOT a Neuron. System cannot proceed like this and will terminate!")

                            output.append(self.network[i].process()) # Append the output of each neuron to the output list


                    else:
                        for i in range(len(self.network)): # Iterate through each neuron. <-- This is the normal case for non-specific regions.

                            if not isinstance(self.network[i], Neuron) or self.network[i] is None: # Type check to make sure neuron exists and is a Neuron.
                                    raise TypeError(f"Critical Error: Object at Index {i} is NOT a Neuron. System cannot proceed like this and will terminate!")

                            self.network[i].process() # Run the neuron's run method




            self.time.counter += 1 # Increment the time counter

        if isinstance(output, list) and output is not None: # Check if the output exists and is of type list.
            return output

        return None

