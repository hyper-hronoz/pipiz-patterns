class IErrorHandler(object):
    """Абстрактный класс обработчика"""

    def handle(self, code):
        raise NotImplementedError()


class Error100Handler(IErrorHandler):
    """Обработчик для кода 100"""

    def handle(self, code):
        if code == 100:
            return 'Error with code 100'


class Error200Handler(IErrorHandler):
    """Обработчик для кода 200"""

    def handle(self, code):
        if code == 200:
            return 'Error with code 200'


class Error400Handler(IErrorHandler):
    """Обработчик для кода 400"""

    def handle(self, code):
        if code == 400:
            return 'Error with code 400'


class Client(object):
    def __init__(self):
        self._handlers = []

    def add_handler(self, h):
        self._handlers.append(h)

    def process(self, code):
        for h in self._handlers:
            msg = h.handle(code)
            if msg:
                print(f'Response: {msg}')
                break
        else:
            print(f'Thise code={code} has not been processed')


client = Client()
client.add_handler(Error100Handler())
client.add_handler(Error200Handler())
client.add_handler(Error400Handler())
client.process(100)
client.process(200)
client.process(500)

