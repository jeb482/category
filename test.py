import unittest
import util

class TestComposition(unittest.TestCase):

    def test_composition_respects_id(self):
        objects = ['A', 1, {"key": 3}]
        for object in objects:
            self.assertTrue(object == util.compose(util.id, util.id)(object))     


if __name__ == '__main__':
    unittest.main()