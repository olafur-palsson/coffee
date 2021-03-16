from decimal import Decimal

from coffee_machine import CoffeeMachine, CoffeeMachineConfig, CoffeeDrink

if __name__ == '__main__':
    config = CoffeeMachineConfig(
        water=200,
        coffee=200,
        milk=200,
        drinks=[
            CoffeeDrink(
                id='espresso-1',
                milk=0,
                coffee=50,
                water=10,
                price=Decimal('3.20'),
                title='Espresso'
            ),
            CoffeeDrink(
                id='latte-1',
                milk=30,
                coffee=20,
                water=10,
                price=Decimal('2.20'),
                title='Latte'
            )
        ]
    )
    machine = CoffeeMachine(config)
    machine.make_drink('espresso-1')


