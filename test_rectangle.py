import unittest

from Test_python.Unit_tests.rectangle import area, perimeter


class RectangleTestCase(unittest.TestCase):
    def test_area_rectangle(self):
        self.assertEqual(area(5, 3), 15)

    def test_area_square(self):
        self.assertEqual(area(4, 4), 16)

    def test_area_zero_side(self):
        self.assertEqual(area(7, 0), 0)

    def test_area_one_by_one(self):
        self.assertEqual(area(1, 1), 1)

    def test_perimeter_rectangle(self):
        self.assertEqual(perimeter(5, 3), 16)

    def test_perimeter_square(self):
        self.assertEqual(perimeter(4, 4), 16)

    def test_perimeter_zero_side(self):
        self.assertEqual(perimeter(7, 0), 14)

    def test_perimeter_one_by_one(self):
        self.assertEqual(perimeter(1, 1), 4)


if __name__ == "__main__":
    unittest.main()
