class Animal:
    def __init__(self, attrs):
        self.attributes = attrs

    def eat(self):
        print('mmmm... delicious!')


class Cat(Animal):
    def eat(self, amount = 0.1):
        if amount > 0.3:
            print('It is so much for me!')
        else:
            print('meow... delicious!')


class Dog(Animal):
    def eat(self):
        print('woof... delicious! woof...')


sharik = Dog({'name': 'Sharik', 'age': 3})
rex = Dog({'name': 'Rex', 'age': 2})
cat = Cat(('Barsik', 1))

# animals = (sharik, rex, cat)
animals = (sharik, rex)

for animal in animals:
    if animal.attributes['age'] > 2:
        print(animal.attributes['name'])
    animal.eat()
