from dataclasses import dataclass
from numbers import Number

@dataclass
class Mitochondrion:
    """
    The Mitochondrion class. Provides functionalities for consuming energy and recharging itself.
    Vital component for the Neural Networks energy management system.
    Can determine whether and action (Action Potential, Neuro Transmitter Synthesis) can be executed or not.
    This Dataclass is a simplified version of a biological Mitochondrion, as most details and subcomponents of
    biological Mitochondria got abstracted away due to runtime efficiency.


    :param capacity: Float: Determines the maximum charge amount the Mitochondrion can reach. Default is 100.0
    :param recharge_rate: Float: Determines how much charge the Mitochondrion recharges per timestep. Default is 0.5
    :param efficiency_lambda: Float: Determines how much energy is uses per request. Default is 1.0


    Late-initialized Properties:
    :property current_charge: Float: The current charge of the Mitochondrion. Is set to the Mitochondrion's max capacity at initialization.

    :author: CallMeMosaic
    :since: 0.0.1
    :version: 0.0.2

    Changelog:
    - 0.0.2: Changed Documentation and Type Checks.
    """
    def __init__(self,
                 capacity: float = 100.0,
                 recharge_rate: float = 0.5,
                 efficiency_lambda: float = 1.0
                 ):

        # Ensure proper Typing for capacity

        if capacity is not None:

            if isinstance(capacity,Number) and not isinstance(capacity, bool):

                if capacity <= 0:
                    raise ValueError("Capacity must be greater than 0!")

                capacity = float(capacity)

            else:
                raise TypeError("Capacity must be instance of class Number!")

        else:
            raise TypeError("Capacity cannot be None!")

        self.capacity = capacity


        # Ensure proper Typing for recharge_rate

        if recharge_rate is not None:

            if isinstance(recharge_rate, Number) and not isinstance(recharge_rate, bool):

                if recharge_rate <= 0:
                    raise ValueError("Recharge Rate must be greater than 0!")

                recharge_rate = float(recharge_rate)

            else:
                raise TypeError("Recharge Rate must be instance of class Number!")

        else:
            raise TypeError("Recharge Rate cannot be None!")

        self.recharge_rate = recharge_rate


        # Ensure proper Typing for efficiency_lambda

        if efficiency_lambda is not None:

            if isinstance(efficiency_lambda, Number) and not isinstance(efficiency_lambda, bool):

                if efficiency_lambda <= 0:
                    raise ValueError("Efficiency Lambda must be greater than 0!")

                efficiency_lambda = float(efficiency_lambda)

            else:
                raise TypeError("Efficiency Lambda must be instance of class Number!")

        else:
            raise TypeError("Efficiency Lambda cannot be None!")

        self.efficiency_lambda = efficiency_lambda


        # Set current charge to max value

        self.current_charge = self.capacity


    """
    ————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
    """


    def consume(self,amount: int) -> bool:
        """
        Decrements the current_charge based on given amount parameter and internal efficiency_lambda.
        If the calculation works out, the function returns True, to signal it's calling entity, that the action can be
        executed. If the calculation is not possible, the method returns False, which prevents the desired action from
        being executed.


        :param amount: TransmittersCost: Either a fixed Integer value or a value from the TransmittersCost Enum, which is used to
        deduct charge from the current_charge.
        :return: Returns a boolean value used to control the actions within neurons.
        :rtype: Bool

        Consumption and Runtime:
        Runtime-Function: 8
        Constant Operations: 8
        O-Notation: O(8) / O(7)
        Ω-Notation: Ω(3)
        Θ-Notation: Θ(1)
        FLOPS: 8

        """

        # Ensure that the amount to consume is not 0

        if amount <= 0:

            # Prevents resulting in nothing being consumed
            raise ValueError("Amount must be greater than 0")


        # Calculate actual amount to consume based on efficiency

        effective_amount = amount * self.efficiency_lambda


        # Ensure effective amount is not greater than the current charge

        if self.current_charge < effective_amount:

            print("NOT ENOUGH CHARGE IN MITOCHONDRION")
            return False

        else:

            self.current_charge -= effective_amount
            return True


    """
    ————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
    """

    #TODO: OPTIMIZE CALCULATIONS
    def recharge(self):
        """
        Recharges the Mitochondrion using its recharge_rate and efficiency_lambda. Also uses the min() function
        to ensure the amount never exceeds the maximum capacity of the Mitochondrion.


        :return: None

        Consumption and Runtime:
        Runtime Function: 6
        Constant Operations: 6
        O-Notation: O(6)
        Ω-Notation: Ω(6)
        Θ-Notation: Θ(1)
        FLOPS: 6 (Though Division is slow)

        """
        recharge_actual = (self.recharge_rate / self.efficiency_lambda) + self.current_charge # UNOPTIMIZED LARGE OVERHEAD DUE TO DIVISION
        self.current_charge = recharge_actual if recharge_actual < self.capacity else self.capacity # more optimized than min()


    """
    ————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
    """


    def what_are_you(self):
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

    def recharge(self) -> None:
        return None

    def what_are_you(self):
        print("I AM.")
