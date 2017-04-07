import unittest

import shapes


class TestRegularPolygon(unittest.TestCase):

	def setUp(self):
		self.square = shapes.RegularPolygon(4, 1)

	def test_triangle_perimeter(self):
		self.assertEqual(self.square.perimeter, 4)

	def test_triangle_apothem(self):
		self.assertEqual(self.square.apothem, 0.5000000000000001)

	def test_triangle_area(self):
		self.assertEqual(self.square.area, 1.0000000000000002)


if __name__ == "__main__":
	unittest.main()