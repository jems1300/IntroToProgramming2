from abc import ABC

from Crustacean import Crustacean


class Krill(Crustacean, ABC):
    def __init__(self, name="Mr. Krabs", num_legs=2, claw=False):
        super().__init__(name, num_legs, claw)

    def __str__(self):
        return (f"{self.get_name()} swims in Bikini Bottom "
                f"and scams SpongeBob below the minimum "
                f"wage")

