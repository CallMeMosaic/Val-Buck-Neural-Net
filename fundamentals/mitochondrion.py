from dataclasses import dataclass

from fundamentals.transmitters_cost import TransmittersCost


@dataclass
class Mitochondrion:
    """
    Represents a Mitochondrion object with properties for energy capacity, recharge rate,
    and energy efficiency. Provides methods to consume and recharge energy.

    This class models a simplified representation of a mitochondrion's energy system.
    It includes attributes to define the maximum energy capacity, the rate at which it
    recharges, and the efficiency with which energy is consumed. The object allows
    energy consumption and recharge operations while adhering to defined constraints.

    :ivar capacity: Maximum energy capacity of the mitochondrion.
    :type capacity: Float
    :ivar recharge_rate: Rate at which energy is replenished in the mitochondrion per unit time.
    :type recharge_rate: Float
    :ivar efficiency_lambda: Efficiency factor for energy usage. A value less than 1.0
        indicates less efficient energy use.
    :type efficiency_lambda: Float
    :ivar current_charge: Tracks the current amount of energy available in the mitochondrion.
    :type current_charge: Float

    :author: CallMeMosaic
    :since: 0.0.1
    :version: 0.0.1
    """
    def __init__(self,
                 capacity: float = 100.0, # Determines max charge of the mitochondrion
                 recharge_rate: float = 0.5, # Determines how fast the mitochondrion recharges
                 efficiency_lambda: float = 0.5 # Determines how much of the energy is used <1 means less energy consumed
                 ):
        if capacity <= 0:
            raise ValueError("Capacity must be greater than 0")
        self.capacity = capacity

        if recharge_rate <= 0:
            raise ValueError("Recharge rate must be greater than 0")
        self.recharge_rate = recharge_rate

        if efficiency_lambda < 0:
            raise ValueError("Efficiency lambda must be greater than 0")
        self.efficiency_lambda = efficiency_lambda

        # change the current charge to it's max
        self.current_charge = capacity

    def consume(self,amount: TransmittersCost) -> bool:
        """
        Consumes an amount of charge based on a given efficiency. The function determines if there is enough charge available to
        perform the requested operation and deducts from the current charge if possible.

        :param self: The current instance of the class.
        :param amount: The amount of charge needed to perform the operation.
        :type amount: Float
        :return: A boolean value indicating whether the operation was successful. Returns True if the charge was successfully
            consumed, and False if there was not enough charge available.
        :rtype: Bool
        :raises ValueError: If the provided amount is not greater than zero.
        """

        # Ensure that the amount to consume is not 0
        if self.amount <= 0:
            # Prevents division by zero
            raise ValueError("Amount must be greater than 0")

        # Calculate actual amount to consume based on efficiency
        effective_amount = amount / self.efficiency_lambda

        # Ensure effective amount is not greater than the current charge
        if self.current_charge <= effective_amount:
            print("NOT ENOUGH CHARGE IN MITOCHONDRION")
            return False
        else:
            self.current_charge -= effective_amount
            return True

    def recharge(self, amount: float) -> None:
        """
        Recharges the current charge of the object with the specified amount, ensuring that
        the charge does not exceed its maximum capacity.

        :param self: The instance of the object on which this method is called.
        :param amount: The amount of charge to be added. Must be a floating-point number.
        :return: None
        """
        self.current_charge = min(self.current_charge + amount, self.capacity)

    def what_are_you():
        print("I am a mitochondrion, the powerhouse of the cell!")


class GodMitochondrion(Mitochondrion):

    """
    Extends the Mitochondrion class with a god-mode variant that ignores
    consumption and recharge constraints.
    """

    DEFAULT_CAPACITY = 100.0
    DEFAULT_RECHARGE_RATE = 1.0
    DEFAULT_EFFICIENCY_LAMBDA = 1.0

    def __init__(self):
        super().__init__(
            capacity=self.DEFAULT_CAPACITY,
            recharge_rate=self.DEFAULT_RECHARGE_RATE,
            efficiency_lambda=self.DEFAULT_EFFICIENCY_LAMBDA
        )

    def consume(self, amount: float) -> bool:
        return True

    def recharge(self, amount: float) -> None:
        return None
