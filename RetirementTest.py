from RetirementCalc import retirementCalc
import unittest

class RetirementTest(unittest.TestCase):

    def retirementCalcTest(self):

        agemet = retirementCalc(25, 6500, .5, 150000)
        self.assertEqual(agemet, (59.0, False))

        agemet = retirementCalc(10, 5, .1, 1000000)
        self.assertEqual(agemet,(1481491.0, True))

        agemet = retirementCalc(50, 100000, .4, 1500000)
        self.assertEqual(agemet,(78.0, False))

        agemet = retirementCalc(50, 100000, .4, 2700000)
        self.assertEqual(agemet,(100.0, True))

        agemet = retirementCalc(50, 100000, .4, 2650000)
        self.assertEqual(agemet,(99.0, False))


if __name__ == '__main__':
    unittest.main()