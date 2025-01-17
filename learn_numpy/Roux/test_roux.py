import unittest

class TestRout(unittest.TestCase):
    def test_run(self):
        self.assertEqual(self.run(), "88" , "Should be 88")

if __name__ == "__main__":
    unittest.main()