import random
import string


class Human:
    def __init__(self, name, code_of_town, address):
        self.name = name
        self.code_of_town = code_of_town
        self.address = address

    def __str__(self):
        return f'{self.code_of_town}: {self.name}, {self.address}'


def name_random_string():
    chars = string.ascii_lowercase
    return ''.join([random.choice(chars) for i in range(8)])


names = [name_random_string() for i in range(10)]
addresses = ['Moscow', 'St. Petersburg', 'Kaluga', 'Obninsk']

data = []
for name in names:
    code_of_town = addresses.index(random.choice(addresses))
    data.append(tuple([name, code_of_town, addresses[code_of_town]]))
print(data)


humans = []
for human in data:
    humans.append(Human(human[0], human[1], human[2]))

print('-'*10)
for human in humans:
    print(human)
