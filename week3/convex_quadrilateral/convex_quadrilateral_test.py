import unittest
from convex_quadrilateral import four_lines_area, lines_intersection, distance, quadrangle_area

class TestConvexQuadrilateral(unittest.TestCase):
    def test_lines_intersection(self):
        self.assertEqual(lines_intersection(1, 0, -1, 0), (0, 0))
        self.assertEqual(lines_intersection(1, 0, 1, 0), None)
        self.assertEqual(lines_intersection(1, 0, 1, 1), None)
        self.assertEqual(lines_intersection(0, 0, 0, 1), None)

    def test_distance(self):
        self.assertEqual(distance(0, 0, 1, 1), 1.41)
        self.assertEqual(distance(0, 0, 0, 0), 0)
        self.assertEqual(distance(-1, -1, 1, 1), 2.83)
        self.assertEqual(distance(1, 2, 3, 4), 2.83)

    def test_quadrangle_area(self):
        self.assertEqual(quadrangle_area(1, 1, 1, 1, 1.41, 1.41), 0.99)
        self.assertEqual(quadrangle_area(1, 2, 1, 2, 2.24, 2.24), 2.01)
        self.assertEqual(quadrangle_area(1, 1, 1, 1, 1, 1), 0.5)
        self.assertEqual(quadrangle_area(1, 1, 1, 1, 2, 2), 2.0)
        self.assertEqual(quadrangle_area(0, 0, 0, 0, 0, 0), None)

    def test_four_lines_area(self):
        self.assertEqual(four_lines_area(1, 0, -1, 0, 1, -2, -1, 2), 2.0)
        self.assertEqual(four_lines_area(1, 0, 1, 1, 1, 2, 1, 3), 0)
        self.assertEqual(four_lines_area(0, 0, 0, 1, 0, 2, 0, 3), 0)
        self.assertEqual(four_lines_area(1, 0, -1, 0, 1, 1, -1, 1), 0.5)
        self.assertEqual(four_lines_area(1, 0, 1, 1, 1, 1, 1, 1), 0)

if __name__ == '__main__':
    unittest.main()