from dataclasses import dataclass
from decimal import Decimal
from typing import List


@dataclass
class CoffeeDrink:
    id: str
    title: str
    coffee: int
    water: int
    milk: int
    price: Decimal


@dataclass
class CoffeeMachineConfig:
    drinks: List[CoffeeDrink]
    water: int
    milk: int
    coffee: int


class CoffeeMachine:
    config: CoffeeMachineConfig

    def __init__(self, config: CoffeeMachineConfig):
        self.config = config

    def add_water(self, amount: int):
        self.config.water += amount

    def get_drinks(self):
        return self.config.drinks

    async def make_drink(self, drink_id: str):
        drink = next(
            drink
            for drink in self.config.drinks
            if drink.id == drink_id)
        await self.get_money_from_customer(drink.price)
        self.brew(drink)

    async def get_money_from_customer(self, amount: Decimal):
        # Do something
        pass

    def brew(self, drink: CoffeeDrink):
        # Do something
        pass
