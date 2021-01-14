import unittest
from task_3 import TestArray


class TestArrays(unittest.TestCase):
    def setUp(self):
        self.array = TestArray(5, [1, 23, 4, 5,5])

    def test_find_first_max(self):
        self.assertEqual(self.array.find_first_max(), 23)

    def test_find_second_max(self):
        self.assertEqual(self.array.find_second_max(), 5)
