import unittest
from convex_ai import lines_intersection, distance, quadrangle_area, four_lines_area
import coverage

# cov = coverage.coverage()
# cov.start()

class TestConvexQuadrilateral(unittest.TestCase):

    def test_lines_intersection(self):
        self.assertIsNone(lines_intersection('l', 'j', 'j', 'k'))
        self.assertEqual(lines_intersection(1, 2, 3, 4), (-1, 1))
        self.assertEqual(lines_intersection(0, 0, 1, 1), (-1.0, 0))

    def test_distance(self):
        self.assertIsNone(distance('l', 'j', 'j', 'k'))
        self.assertEqual(distance(1, 2, 4, 6), 5.0)
        self.assertEqual(distance(0, 0, 1, 1), 1.41)

    def test_quadrangle_area(self):
        self.assertIsNone(quadrangle_area('l', 'j', 'j', 'k', 'j', 'k'))
        self.assertIsNone(quadrangle_area(1, 1, 2, 1, 1, 2))
        self.assertIsNone(quadrangle_area(1, 1, 2, 1, 2, 2 * (1 + 2 ** 2) ** 0.5))

    def test_four_lines_area(self):
        self.assertIsNone(four_lines_area('l', 'j', 'j', 'k', 'j', 'k', 'j', 's'))
        self.assertIsNone(four_lines_area(1, 2, 3, 4, 3, 4, 5, 6))
        self.assertIsNone(four_lines_area(0, 0, 1, 1, 1, 1, 0, 2))
        self.assertIsNone(four_lines_area(1, 1, 1, 2, 2, 1, 1, 0))
        self.assertIsNone(four_lines_area(1, 10, -1, 10, 1, -10, -1, -10))

# cov.stop()
# cov.report()
# if __name__ == '__main__':
#     unittest.main()