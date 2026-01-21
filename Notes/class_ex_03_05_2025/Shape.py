#To make shape an abstract class
from abc import ABC, abstractmethod
class Shape(ABC):
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    @abstractmethod
    def area(self):
        pass

    def 


    # Later when we extend the class, we can implement the actual method

# This is our general shape class