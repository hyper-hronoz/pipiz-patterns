from abc import ABC, abstractmethod

class Pizza(ABC):
    _pizza_name: str
    _pizza_cost: int

    def __init__(self, pizza_name: str, pizza_cost: int) -> None: 
        self._pizza_name = pizza_name
        self._pizza_cost = pizza_cost

    def get_cost(self) -> int:
        return self._pizza_cost

class Pizza_Decorator(Pizza):
    _pizza: Pizza

    def __init__(self, pizza: Pizza) -> None:
        self._pizza = pizza

    @abstractmethod
    def decorate_pizza(self) -> None:
        pass

class Cheese_Decorator(Pizza_Decorator):
    def __init__(self, pizza: Pizza) -> None:
        super().__init__(pizza)
        self.decorate_pizza()

    def decorate_pizza(self) -> None:
        self._pizza._pizza_cost += 10
        self._pizza._pizza_name += " fucking cheese"


if __name__ == "__main__":
    default_pizza = Pizza("Peperonni", 20);
    cheese_pizza = Cheese_Decorator(default_pizza);
    print(cheese_pizza._pizza._pizza_cost)
