import unittest
from find import find_pair
from data import nums, target

class Find(unittest.TestCase):
    def test_find_pair(self):
        pairs = find_pair(nums, target)
        self.assertEqual(pairs, [(0, 12), (-4, 16), (5, 7)])
    