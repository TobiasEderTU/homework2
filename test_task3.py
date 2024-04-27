#!/usr/bin/env python3

""" Test for Task3: Checking the functionality in 'task3.py' using assertions """

import unittest
import task3


class Test(unittest.TestCase):
    def setUp(self) -> None:

        self.a1 = -5
        self.b1 = -3
        self.c1 = 2
        self.d1 = 1

        self.a2 = 1
        self.b2 = -1
        self.c2 = -2
        self.d2 = -2

        self.x1 = -3
        self.x2 = 2

    def test_eval_poly_order2(self):

        self.assertEqual(task3.eval_poly_order2(
            self.x1, self.a1, self.b1, self.c1), 22)
        self.assertEqual(task3.eval_poly_order2(
            self.x2, self.a1, self.b1, self.c1), -3)
        self.assertEqual(task3.eval_poly_order2(
            self.x1, self.a2, self.b2, self.c2), -14)
        self.assertEqual(task3.eval_poly_order2(
            self.x2, self.a2, self.b2, self.c2), -9)

    def test_eval_poly_order3(self):
        self.assertEqual(task3.eval_poly_order3(
            self.x1, self.a1, self.b1, self.c1, self.d1), -5)
        self.assertEqual(task3.eval_poly_order3(
            self.x2, self.a1, self.b1, self.c1, self.d1), 5)
        self.assertEqual(task3.eval_poly_order3(
            self.x1, self.a2, self.b2, self.c2, self.d2), 40)
        self.assertEqual(task3.eval_poly_order3(
            self.x2, self.a2, self.b2, self.c2, self.d2), -25)


if __name__ == "__main__":
    unittest.main()
