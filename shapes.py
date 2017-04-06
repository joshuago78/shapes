from math import tan as tangent
from math import radians


class RegularPolygon():
    # A regular shape has sides of equal length

    num_sides = None
    
    def __init__(self, side_length):
        self.side_length = side_length

    @property
    def perimeter(self):
        return self.num_sides * self.side_length

    @property
    def apothem(self):
        rads = radians(180/self.num_sides)
        return self.side_length / (2 * tangent(rads))

    @property
    def area(self):
        return (self.perimeter * self.apothem) / 2


class RegularTriangle(RegularPolygon):
    
    num_sides = 3


class Square(RegularPolygon):

    pass


class RegularPentagon(RegularPolygon):

    pass


class RegularHexagon(RegularPolygon):

    pass


class RegularSeptagon(RegularPolygon):

    pass


class RegularOctagon(RegularPolygon):

    pass


class RegularNonagon(RegularPolygon):

    pass


class RegularDecagon(RegularPolygon):

    pass