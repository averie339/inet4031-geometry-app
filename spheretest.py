import unittest
import sphere

class sphereTest(unittest.TestCase):

    def test_volume1(self):
        self.assertAlmostEqual(sphere.volume(1), 4.18879, places=5)

    def test_volume2(self):
        self.assertAlmostEqual(sphere.volume(3), 113.097, places=3)

    def test_volume3(self):
        self.assertAlmostEqual(sphere.volume(10), 4188.79, places=2)

if __name__ == '__main__':
    unittest.main()
