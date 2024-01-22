import copy
from abc import ABC, abstractmethod


class Prototype(ABC):
    @abstractmethod
    def proto_copy(self) -> None:
        pass

class Human(Prototype):
    _age: int
    _skin_color: int

    def __init__(self, age, skin_color) -> None:
        self._age = age
        self._skin_color = skin_color

    def set_skin_color(self, skin_color) -> None:
        self._skin_color = skin_color

    def get_skin_color(self) -> int:
        return self._skin_color

    def proto_copy(self):
        return copy.deepcopy(self)

if __name__ == "__main__":
    human = Human(12, 0xffffff)
    human_prototype = human.proto_copy();
    human_prototype.set_skin_color(0x000000)
    print("Whine human", human, human.get_skin_color())
    print("NIger", human_prototype, human_prototype.get_skin_color())
