import unittest
from test_say import SayTest

if __name__ == "__main__":
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(SayTest)
    unittest.TextTestRunner().run(suite)