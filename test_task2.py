#!/usr/bin/env python3

""" Test for Task2: Checking the functionality in 'task2.py' using assertions """

import unittest
import task2


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.a = 10.0
        self.b = -5.0
        self.c = 2.5
        self.d = -4.2
        self.e = 15.0

    def test_sum2(self):
        self.assertEqual(task2.sum2(self.a, self.b), 5.0)
        self.assertAlmostEqual(task2.sum2(self.b, self.d), -9.2)

    def test_sum3(self):
        self.assertAlmostEqual(task2.sum3(self.a, self.b, self.c), 7.5)
        self.assertAlmostEqual(task2.sum3(self.a, self.b, self.d), 0.8)

    def test_abssum2(self):
        self.assertAlmostEqual(task2.abssum2(self.a, self.b), 15.0)
        self.assertAlmostEqual(task2.abssum2(self.a, self.c), 12.5)

    def test_abssum3(self):
        self.assertAlmostEqual(task2.abssum3(self.a, self.b, self.c), 17.5)
        self.assertAlmostEqual(task2.abssum3(self.b, self.d, self.e), 24.2)

    def test_mult5(self):
        self.assertAlmostEqual(task2.mult5(
            self.a, self.b, self.c, self.d, self.e), 7875.0)


if __name__ == "__main__":
    unittest.main()
