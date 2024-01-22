class Paper:
    def __init__(self, count=0):
        self._count = count

    def get_count(self):
        return self._count

    def draw(self, text):
        if self._count > 0:
            self._count -= 1
            print(text)


class Printer:
    def error(self, msg):
        print(f'Ошибка: {msg}')

    def print(self, paper, text):
        if paper.get_count() > 0:
            paper.draw(text)
        else:
            self.error('Бумага закончилась')


class Facade(object):
    def __init__(self):
        self._printer = Printer()
        self._paper = Paper(1)

    def write(self, text):
        self._printer.print(self._paper, text)


f = Facade()
f.write('Hello world!')
f.write('Hello world!')
