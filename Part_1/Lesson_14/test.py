import unittest
from Class_work14 import *

# class TestFunc(unittest.TestCase):

#     def test_sum_func(self):
#         self.assertEqual(sum_calc([1,2,3]), 6)

#     def test_sqrt_func(self):
#         self.assertEqual(sqrt_calc(10), 100)


class TestFunc1(unittest.TestCase):

    def test_multi_calc(self):
        self.assertEqual(multi_calc([1, 2, 3]), 6)

    def test_multi_calc1(self):
        self.assertEqual(multi_calc((1, 2, 3, 4)), 24)

# if __name__ == "__main__":
#     unittest.main()

print(dir(TestFunc1))