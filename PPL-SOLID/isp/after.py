class Mammal:
    def __init__(self, name):
        self.name = name


class SwimmerInterface:
    def swim(self):
        pass


class WalkerInterface:
    def walk(self):
        pass


class TalkerInterface:
    def talk(self):
        pass


class Human(Mammal, SwimmerInterface, WalkerInterface, TalkerInterface):
    def __init__(self, name):
        super().__init__(name)

    def swim(self):
        print(f"I'm {self.name} and I can swim")

    def walk(self):
        print(f"I'm {self.name} and I can walk")

    def talk(self):
        print(f"I'm {self.name} and I can talk")


class Dog(Mammal, SwimmerInterface, WalkerInterface):
    def __init__(self, name):
        super().__init__(name)

    def swim(self):
        print(f"I'm {self.name} and I can swim")

    def walk(self):
        print(f"I'm {self.name} and I can walk")


human = Human('Ivan')
human.swim()
human.walk()
human.talk()

dog = Dog('Sharik')
dog.swim()
dog.walk()

