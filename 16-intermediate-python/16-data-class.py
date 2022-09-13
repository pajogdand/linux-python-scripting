# from dataclasses import dataclass
# @dataclass
# class LinkManagerConfig:
#     """LinkManager configuration settings."""
#
#     # When True, automatically capture ALA data on failed link training attempts
#     AlaFtdc: bool = False
#
#     # When True, automatically attempt to retrain links when a link drop is detected
#     BasicLinkRecovery: bool = True
#
# def main():
#     LinkManagerConfig
#
# if __name__ == "__main__":
#     main()
# ======================================================
from dataclasses import dataclass

@dataclass
class InventoryItem:
    """Class for keeping track of an item in inventory."""
    name: str
    unit_price: float
    quantity_on_hand: int = 0

    def total_cost(self) -> float:
        return self.unit_price * self.quantity_on_hand

P=InventoryItem("Paneer" , 102.0 , 5)
print(P.total_cost())

C=InventoryItem("Cheese" , 120.0 , 1)
print(C.total_cost())


print(P, C)
