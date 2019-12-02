from math import tan as tangent #changes are made to the area method
from math import radians


class RegularPolygon():
    # A regular shape has sides of equal length
    
    def __init__(self, side_length, num_sides=None):
        if side_length <= 0:
            raise Exception('Side length must be greater than zero')
        self.side_length = side_length
        if num_sides:
            if num_sides < 3:
                raise Exception('A polygon must have at least 3 sides')
            self.num_sides = num_sides

    @property
    def perimeter(self):
        return self.num_sides * self.side_length

    @property
    def apothem(self):
        rads = radians(180/self.num_sides)
        return self.side_length / (2 * tangent(rads))

    @property
    def area(self):
        return (self.perimeter * self.apothem) /2


class RegularTriangle(RegularPolygon):
    
    num_sides = 3


class Square(RegularPolygon):

    num_sides = 4


class RegularPentagon(RegularPolygon):

    num_sides = 5
    @property
    def apothem(self):
        rads = radians(180/self.num_sides)
        return self.side_length / (2 * tangent(rads))

    @property
    def area(self):
        return (self.perimeter * self.apothem) /2

class RegularHexagon(RegularPolygon):

    num_sides = 6

    @property
    def apothem(self):
        rads = radians(180 / self.num_sides)
        return self.side_length / (2 * tangent(rads))


class RegularSeptagon(RegularPolygon):

    num_sides = 7


class RegularOctagon(RegularPolygon):

    num_sides = 8


class RegularNonagon(RegularPolygon):

    num_sides = 9


class RegularDecagon(RegularPolygon):

    num_sides = 10

