import unittest

def mystery_function(lst):
    result = lst
    for i in range(len(lst)):
        if lst[i] % 2 == 0:
            result[i] = lst[i] ** 2
    return result

class TestForDebug(unittest.TestCase):
    def test_1(self):
        self.assertEqual(mystery_function([1, 2, 3, 4, 5]), [1, 4, 3, 16, 5])
    
    def test_2(self):
        self.assertEqual(mystery_function([4, 1, 6, 2, 10]), [16, 1, 36, 4, 100])

if __name__ == "__main__":
    unittest.main()