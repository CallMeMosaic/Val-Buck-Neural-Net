"""
Mathematical Constants needed for calculations such as cable theory or leaky function.

"""

#def MEMBRANE_CAPACITANCE()


DELTA_T = 0.2 # Time it takes for one timestep to finish fully (should be accurate, as it is the global time constant)

SOMA_TAU_MEMBRANE = 1727875.9594743862 # Derived from putting soma values in a dendrite and taking it tau_membrane: Values were: -52 Threshold, -70 Resting Potential, 5 Width, 5 Length, 22k Membrane Resistence (As according to google)
SOMA_LEAK_FACTOR = DELTA_T / SOMA_TAU_MEMBRANE




# COST CONSTANTS FOR NON TRANSMITTERS
COST_STANDARD = 1
COST_FIRE = 5
COST_FAILED_OPERATION = 1
COST_TRANSPORT_INTERNALLY = 2
COST_BUILD_SYNAPSE = 15



