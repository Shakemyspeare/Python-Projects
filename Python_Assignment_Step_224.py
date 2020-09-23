from abc import ABC, abstractmethod

class Computer(ABC):
    @abstractmethod
    def compute(self):
        pass
    def power(self):
        print("There is power to your machine.")

class Desktop(Computer):
    def compute(self):
        x = 1
        y = 2
        print("If x is equal to {} and y is equal to {} then x + y is equal to {}!".format(x, y, x+y))


com1 = Desktop()
com1.power()
com1.compute()