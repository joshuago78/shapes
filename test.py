import unittest

import shapes


class TestTriangle(unittest.TestCase):

	def setUp(self):
		self.triangle = shapes.RegularTriangle(1)

	def test_triangle_perimeter(self):
		self.assertEqual(self.triangle.perimeter, 3)

	def test_triangle_apothem(self):
		self.assertEqual(self.triangle.apothem, 0.288675134594813)

	def test_triangle_area(self):
		self.assertEqual(self.triangle.area, 0.43301270189221946)


if __name__ == "__main__":
	unittest.main()