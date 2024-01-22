class Driver:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Car:
    def __init__(self, driver):
        self.driver = driver

    def drive(self):
        print(f'Car being driven by {self.driver.name}')


class CarProxy:
    def __init__(self, driver):
        self.driver = driver
        self.car = Car(driver)

    def drive(self):
        if self.driver.age >= 16:
            self.car.drive()
        else:
            print('Driver too young')


car1 = CarProxy(Driver('Ivan', 11))
car1.drive()

car2 = CarProxy(Driver('Petr', 22))
car2.drive()

car3 = CarProxy(Driver('Nikolay', 33))
car3.drive()