import random
from abc import ABCMeta, abstractmethod


class IHandler(metaclass=ABCMeta):
    """The Handler Interface that the Successors should implement"""
    @staticmethod
    @abstractmethod
    def handle(payload):
        """A method to implement"""


class Successor1(IHandler):
    """A Concrete Handler"""
    @staticmethod
    def handle(payload):
        test = random.randint(1, 3)
        print(f"Successor1 payload = {payload:4.1f} with test value = {test}")
        if test == 1:
            payload = payload + 1
            payload = Successor1().handle(payload)
        if test == 2:
            payload = payload - 1
            payload = Successor2().handle(payload)
        return payload


class Successor2(IHandler):
    """A Concrete Handler"""
    @staticmethod
    def handle(payload):
        test = random.randint(1, 3)
        print(f"Successor2 payload = {payload:4.1f} with test value = {test}")
        if test == 1:
            payload = payload * 2
            payload = Successor1().handle(payload)
        if test == 2:
            payload = payload / 2
            payload = Successor2().handle(payload)
        return payload


class Chain:
    """A chain with a default first successor"""
    @staticmethod
    def start(payload):
        """Setting the first successor that will modify the payload"""
        return Successor1().handle(payload)


# The Client
chain = Chain()
PAYLOAD = 5
out = chain.start(PAYLOAD)
print(f'Finished result = {out}')
