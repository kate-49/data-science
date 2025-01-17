import unittest
import roux as r
import numpy as np

class TestRout(unittest.TestCase):
    def test_run(self):

        self.assertTrue(np.array_equal(r.Roux(5).run(),np.array([9, 0, 4, 0, 1])))
        self.assertTrue(np.array_equal(r.Roux(8).run(),np.array([0, 16, 0, 9, 0, 4, 0, 1])))
        self.assertTrue(np.array_equal(r.Roux(12).run(),np.array([0, 36, 0, 25,  0, 16, 0, 9, 0, 4, 0, 1])))

if __name__ == "__main__":
    unittest.main()