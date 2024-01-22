import copy


class Address:
    def __init__(self, street_address, city, country):
        self.country = country
        self.city = city
        self.street_address = street_address

    def __str__(self):
        return f'{self.street_address}, {self.city}, {self.country}'


class Person:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def __str__(self):
        return f'{self.name} lives at {self.address}'


p1 = Person("Ivan", Address("Kirova st.", "Kaluga", "Russian Federation"))
print(p1)
p2 = copy.deepcopy(p1)
p2.name = "Maria"
p2.address.street_address = "Plekhanova st."
print(p1, p2, sep='\n')