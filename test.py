import unittest

import shapes


class TestRegularPolygon(unittest.TestCase):

    def setUp(self):
        self.shape = shapes.RegularPolygon(1, 3)

    def test_shape_perimeter(self):
        self.assertEqual(self.shape.perimeter, 3)

    def test_shape_apothem(self):
        self.assertEqual(self.shape.apothem, 0.288675134594813)

    def test_shape_area(self):
        self.assertEqual(self.shape.area, 0.43301270189221946)

    def test_side_size_error(self):
        self.assertRaises(Exception, shapes.RegularPolygon, (-1, 4))

    def test_side_num_error(self):
        self.assertRaises(Exception, shapes.RegularPolygon, (1, 2))        


class TestTriangle(unittest.TestCase):

    def setUp(self):
        self.triangle = shapes.RegularTriangle(1)

    def test_triangle_perimeter(self):
        self.assertEqual(self.triangle.perimeter, 3)

    def test_triangle_apothem(self):
        self.assertEqual(self.triangle.apothem, 0.288675134594813)

    def test_triangle_area(self):
        self.assertEqual(self.triangle.area, 0.43301270189221946)


class TestSquare(unittest.TestCase):

	def setUp(self):
		self.square = shapes.Square(1)

	def test_square_perimeter(self):
		self.assertEqual(self.square.perimeter, 4)

	def test_square_apothem(self):
		self.assertEqual(self.square.apothem, 0.5000000000000001)

	def test_square_area(self):
		self.assertEqual(self.square.area, 1.0000000000000002)


class TestPentagon(unittest.TestCase):

    def setUp(self):
        self.pentagon = shapes.RegularPentagon(1)
        self.regpoly5 = shapes.RegularPolygon(1, 5)

    def test_pentagon_perimeter(self):
        self.assertEqual(self.pentagon.perimeter, 5)

    def test_pentagon_apothem(self):
        self.assertEqual(self.pentagon.apothem, self.regpoly5.apothem)

    def test_pentagon_area(self):
        self.assertEqual(self.pentagon.area, self.regpoly5.area)


class TestHexagon(unittest.TestCase):

    def setUp(self):
        self.hexagon = shapes.RegularHexagon(1)
        self.regpoly6 = shapes.RegularPolygon(1, 6)

    def test_hexagon_perimeter(self):
        self.assertEqual(self.hexagon.perimeter, 6)

    def test_hexagon_apothem(self):
        self.assertEqual(self.hexagon.apothem, self.regpoly6.apothem)

    def test_hexagon_area(self):
        self.assertEqual(self.hexagon.area, self.regpoly6.area)

class TestSeptagon(unittest.TestCase):

    def setUp(self):
        self.septagon = shapes.RegularSeptagon(1)

    def test_septagon_perimeter(self):
        self.assertEqual(self.septagon.perimeter, 7)

    def test_septagon_apothem(self):
        self.assertEqual(self.septagon.apothem, 1.0382606982861684)

    def test_septagon_area(self):
        self.assertEqual(self.septagon.area, 3.6339124440015893)


class TestOctagon(unittest.TestCase):

    def setUp(self):
        self.octagon = shapes.RegularOctagon(1)

    def test_octagon_perimeter(self):
        self.assertEqual(self.octagon.perimeter, 8)

    def test_octagon_apothem(self):
        self.assertEqual(self.octagon.apothem, 1.2071067811865475)

    def test_octagon_area(self):
        self.assertEqual(self.octagon.area, 4.82842712474619)


class TestNonagon(unittest.TestCase):

    def setUp(self):
        self.nonagon = shapes.RegularNonagon(1)

    def test_nonagon_perimeter(self):
        self.assertEqual(self.nonagon.perimeter, 9)

    def test_nonagon_apothem(self):
        self.assertEqual(self.nonagon.apothem, 1.3737387097273113)

    def test_nonagon_area(self):
        self.assertEqual(self.nonagon.area, 6.181824193772901)


class TestDecagon(unittest.TestCase):

    def setUp(self):
        self.decagon = shapes.RegularDecagon(1)

    def test_decagon_perimeter(self):
        self.assertEqual(self.decagon.perimeter, 10)

    def test_decagon_apothem(self):
        self.assertEqual(self.decagon.apothem, 1.538841768587627)

    def test_decagon_area(self):
        self.assertEqual(self.decagon.area, 7.694208842938135)        


if __name__ == "__main__":
	unittest.main()