from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetre(self):
        pass


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        print(f'area = {self.side*self.side}')

    def perimetre(self):
        print(f'perimetre = {4*self.side}')


class Rectangle(Shape):
    def __init__(self, len, wid):
        self.len = len
        self.wid = wid

    def area(self):
        print(f'area = {self.len*self.wid}')

    def perimetre(self):
        print(f'perimetre = {2*(self.len+self.wid)}')


sq = Square(4)
sq.area()
sq.perimetre()

req = Rectangle(2,3)
req.area()
req.perimetre()

try:
    sh = Shape()
except BaseException as e:
    print('error: ', e)
