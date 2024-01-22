class Animal:
    def __init__(self, name, age):
        self.attributes = {'name': name, 'age': age}

    def eat(self, _amount=0):
        print('mmmm... delicious!')


class Cat(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def eat(self, amount=0.1):
        if amount > 0.3:
            print('It is so much for me!')
        else:
            print('meow... delicious!')


class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def eat(self, _amount=0):
        print('woof... delicious! woof...')


sharik = Dog('Sharik', 3)
rex = Dog('Rex', 2)
cat = Cat('Barsik', 4)

animals = (sharik, rex, cat)

for animal in animals:
    if animal.attributes['age'] > 2:
        print(animal.attributes['name'])
    animal.eat(0.5)

