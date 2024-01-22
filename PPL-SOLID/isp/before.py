class Mammal:
    def __init__(self, name):
        self.name = name

    def swim(self):
        pass

    def walk(self):
        pass

    def talk(self):
        pass


class Human(Mammal):
    def __init__(self, name):
        super().__init__(name)

    def swim(self):
        print(f"I'm {self.name} and I can swim")

    def walk(self):
        print(f"I'm {self.name} and I can walk")

    def talk(self):
        print(f"I'm {self.name} and I can talk")


class Dog(Mammal):
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
dog.talk()

