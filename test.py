import unittest
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

class TestMathOperations(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(subtract(10, 5), 5)
        self.assertEqual(subtract(0, 5), -5)
        self.assertEqual(subtract(-5, -5), 0)
        self.assertEqual(subtract(0, 0), 0)

if __name__ == '__main__': # pragma: no cover
    unittest.main()