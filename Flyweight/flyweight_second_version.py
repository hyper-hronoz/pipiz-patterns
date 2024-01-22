class Spam(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b


class SpamFactory(object):
    def __init__(self):
        self.__instances = dict()

    def get_instance(self, a, b):
        if (a, b) not in self.__instances:
            self.__instances[(a, b)] = Spam(a, b)
            return self.__instances[(a, b)]

    def __str__(self):
        return '; '.join([str(x) for x in self.__instances])


spamFactory = SpamFactory()
spamFactory.get_instance(1, 1)
spamFactory.get_instance(1, 1)
spamFactory.get_instance(1, 2)
spamFactory.get_instance(1, 2)
spamFactory.get_instance(1, 3)
spamFactory.get_instance(1, 3)
spamFactory.get_instance(3, 1)
spamFactory.get_instance(3, 1)

print(spamFactory)