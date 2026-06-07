from typing import Protocol


class VendingMachine(Protocol):
    def enter_money(): ...

    def choose_drink(): ...

    def restock_cups(): ...

    def restock_drink(): ...

    def change_price(): ...

    def factory_reset(): ...


# DrinkBuyingInterface <: VendingMachine
class DrinkBuyingInterface:
    def enter_money(): ...

    def choose_drink(): ...


class Customer:
    def buy_drink(self, v: DrinkBuyingInterface):  # ISP
        ...


customer = Customer()
v = VendingMachine()

customer.buy_drink(v)
