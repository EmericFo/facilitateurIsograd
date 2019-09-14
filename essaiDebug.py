import unittest
import miseAuPointPourIsograd

class Test(unittest.TestCase):

    def test_env(self):
        miseAuPointPourIsograd.testMoiCa("/Users/emeric/Dev/exo/python/tosa/exo3", "1")
        


if __name__ == '__main__':
    unittest.main()