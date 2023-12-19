import unittest
from fraction import Fraction


class FractionTestCase(unittest.TestCase):
    """
    test all methods of fraction class.

    """
    frac1 = Fraction()
    frac2 = Fraction(5)
    frac3 = Fraction(den=9)
    frac4 = Fraction(-9, -81)
    frac5 = Fraction(-50, 125)
    frac6 = Fraction(3, -8)

    def test_fraction_init(self):
        """
        Test : - the constructor of the class
               - the num of a fraction
               - the den of a fraction
        """
        # checking if default value are correct when no argument are given to the class
        self.assertEqual(self.frac1.numerator, 0, 'Fraction().numerator')
        self.assertEqual(self.frac1.denominator, 1, 'Fraction().denominator')

        # checking if default value are correct when arg is given for num
        self.assertEqual(self.frac2.numerator, 5, 'Fraction(5).numerator')
        self.assertEqual(self.frac2.denominator, 1, 'Fraction(5).denominator')

        # checking if is reduced to 0/1 if no arg is given for num
        self.assertEqual(self.frac3.numerator, 0, 'Fraction(den=9).numerator')
        self.assertEqual(self.frac3.denominator, 1, 'Fraction(den=9).denominator')

        # checking if values are correctly reduced when possible
        self.assertEqual(self.frac5.numerator, -2, 'Fraction(-50, 125).numerator')
        self.assertEqual(self.frac5.denominator, 5), 'Fraction(-50, 125).denominator'

        # checking if values are correctly reduced and absolute when necessary
        self.assertEqual(self.frac4.numerator, 1, 'Fraction(-9,-81)')
        self.assertEqual(self.frac4.denominator, 9, 'Fraction(-9, -81)')

        # checking if values are correctly transformed to a correct fraction way
        self.assertEqual(self.frac6.numerator, -3, 'Fraction(3, -8)')
        self.assertEqual(self.frac6.denominator, 8, 'Fraction(3, -8)')

        with self.assertRaises(ZeroDivisionError, msg='Fraction(59, 0'):
            Fraction(59, 0)

    def test_fraction_str(self):
        """
        Test : - string method of the fraction class
        """
        self.assertEqual(str(self.frac1), '[0/1]', 'str(Fraction())')
        self.assertEqual(str(self.frac2), '[5/1]', 'str(Fraction(5))')
        self.assertEqual(str(self.frac3), '[0/1]', 'str(Fraction(den=9))')
        self.assertEqual(str(self.frac5), '[-2/5]', 'str(Fraction(-125, 50))')
        self.assertEqual(str(self.frac4), '[1/9]', 'str(Fraction(-9, -81))')
        self.assertEqual(str(self.frac6), '[-3/8]', 'str(Fraction(3, -8))')

    def test_fraction_repr(self):
        """
        Test : - the representation of the fraction class

        """
        self.assertEqual(repr(self.frac1), '<Fraction: [0/1]>', 'repr(Fraction())')
        self.assertEqual(repr(self.frac2), '<Fraction: [5/1]>', 'repr(Fraction(5))')
        self.assertEqual(repr(self.frac3), '<Fraction: [0/1]>', 'repr(Fraction(den=9))')
        self.assertEqual(repr(self.frac5), '<Fraction: [-2/5]>', 'repr(Fraction(-50, 125))')
        self.assertEqual(repr(self.frac4), '<Fraction: [1/9]>', 'repr(Fraction(-9, -81))')
        self.assertEqual(repr(self.frac6), '<Fraction: [-3/8]>', 'repr(Fraction(3, -8))')

    def test_fraction_as_mixed_number(self):
        """
        Test the mixed number form of a fraction.
        """
        self.assertEqual(self.frac1.as_mixed_number(), '0 + [0/1]', 'Fraction().as_mixed_number()')
        self.assertEqual(self.frac2.as_mixed_number(), '5 + [0/1]', 'Fraction(5).as_mixed_number()')
        self.assertEqual(self.frac3.as_mixed_number(), '0 + [0/1]', 'Fraction(den=9).as_mixed_number()')
        self.assertEqual(self.frac5.as_mixed_number(), '-1 + [3/5]', 'Fraction(-50, 125).as_mixed_number()')
        self.assertEqual(self.frac4.as_mixed_number(), '0 + [1/9]', 'Fraction(-9, -81).as_mixed_number()')
        self.assertEqual(self.frac6.as_mixed_number(), '-1 + [5/8]', 'Fraction(3, -8).as_mixed_number()')

    def test_fraction_add(self):
        """
        Test to add of a fraction and another fraction or an integer.
        """
        self.assertEqual(self.frac1 + self.frac5, Fraction(-2, 5), 'Fraction() + Fraction(-50, 125)')
        self.assertEqual(self.frac2 + self.frac3, Fraction(5, 1), 'Fraction(5) + Fraction(den=9)')
        self.assertEqual(self.frac4 + self.frac6, Fraction(-19, 72), 'Fraction(-9, -81) + Fraction(3, -8)')
        self.assertEqual(self.frac6 + 1, Fraction(5, 8), 'Fraction(3, -8) + 1')

        with self.assertRaises(ValueError, msg='Fraction() + 1.2'):
            self.frac1 + 1.2

    def test_fraction_sub(self):
        """
        Test to subtract of a fraction and another fraction or an integer.
        """
        self.assertEqual(self.frac1 - self.frac5, Fraction(2, 5), 'Fraction() - Fraction(-50, 125)')
        self.assertEqual(self.frac2 - self.frac3, Fraction(5, 1), 'Fraction(5) - Fraction(den=9)')
        self.assertEqual(self.frac4 - self.frac6, Fraction(35, 72), 'Fraction(-9, -81) - Fraction(3, -8)')
        self.assertEqual(self.frac6 - 1, Fraction(-11, 8), 'Fraction(3, -8) - 1')

        with self.assertRaises(ValueError, msg='Fraction() - 1.2'):
            self.frac1 - 1.2

    def test_fraction_mul(self):
        """
        Test to multiply of a fraction and another fraction or an integer.
        """
        self.assertEqual(self.frac1 * self.frac5, Fraction(0, 1), 'Fraction() * Fraction(-50, 125)')
        self.assertEqual(self.frac2 * self.frac3, Fraction(0, 1), 'Fraction(6) * Fraction(den=9)')
        self.assertEqual(self.frac4 * self.frac6, Fraction(-1, 24), 'Fraction(-9, -81) * Fraction(3, -8)')
        self.assertEqual(self.frac6 * 1, Fraction(-3, 8), 'Fraction(3, -8) * 1')

        with self.assertRaises(ValueError, msg='Fraction() * 1.2'):
            self.frac1 * 1.2

    def test_fraction_truediv(self):
        """
        Test to true division of a fraction and another fraction or an integer.
        """
        self.assertEqual(self.frac1 / self.frac5, Fraction(0, 1), 'Fraction() / Fraction(-50, 125)')
        self.assertEqual(self.frac4 / self.frac6, Fraction(-8, 27), 'Fraction(-9, -81) / Fraction(3, -8)')
        self.assertEqual(self.frac6 / 1, Fraction(-3, 8), 'Fraction(3, -8) / 1')

        with self.assertRaises(ZeroDivisionError, msg='Fraction(5) / Fraction(den=9)'):
            self.frac2 / self.frac3

        with self.assertRaises(ValueError, msg='Fraction() / 1.2'):
            self.frac1 / 1.2

    def test_fraction_pow(self):
        """
        est to power a fraction with an integer
        """
        self.assertEqual(self.frac1 ** -1, Fraction(0, 1), 'Fraction() ** -1')
        self.assertEqual(self.frac4 ** 3, Fraction(1, 729), 'Fraction(-9, -81) ** 3')
        self.assertEqual(self.frac6 ** -2, Fraction(64, 9), 'Fraction(3, -8) ** -2')

    def test_fraction_float(self):
        """
        est the float value of a fraction
        """
        self.assertEqual(float(self.frac1), 0, 'float(Fraction())')
        self.assertEqual(float(self.frac2), 5, 'float(Fraction(5))')
        self.assertEqual(float(self.frac3), 0, 'float(Fraction(den=9))')
        self.assertEqual(float(self.frac5), -2 / 5, 'float(Fraction(-50, 125))')
        self.assertEqual(float(self.frac4), 1 / 9, 'float(Fraction(-9, -81))')
        self.assertEqual(float(self.frac6), -3 / 8, 'float(Fraction(3, -8))')

    def test_fraction_abs(self):
        """
        est the absolute value of a fraction
        """
        self.assertEqual(abs(self.frac1), Fraction(), 'abs(Fraction())')
        self.assertEqual(abs(self.frac2), Fraction(5), 'abs(Fraction(5))')
        self.assertEqual(abs(self.frac3), Fraction(den=9), 'abs(Fraction(den=9))')
        self.assertEqual(abs(self.frac5), Fraction(50, 125), 'abs(Fraction(-50, 125))')
        self.assertEqual(abs(self.frac4), Fraction(9, 81), 'abs(Fraction(-9, -81))')
        self.assertEqual(abs(self.frac6), Fraction(3, 8), 'abs(Fraction(3, -8))')

    def test_fraction_eq(self):
        """
        test if the fraction is equal to another fraction, a float or an integer
        """
        self.assertTrue(self.frac1 == self.frac3, 'Fraction() == Fraction(den=9)')

        self.assertFalse(self.frac2 == self.frac5, 'Fraction(5) == Fraction(-50, 125)')
        self.assertFalse(self.frac4 == self.frac6, 'Fraction(-9, -81) == Fraction(3, -8)')

    def test_fraction_is_zero(self):
        """
        test if the value of the fraction is null
        """
        self.assertTrue(self.frac1.is_zero(), 'Fraction().is_zero()')
        self.assertTrue(self.frac3.is_zero(), 'Fraction(den=9).is_zero()')

        self.assertFalse(self.frac2.is_zero(), 'Fraction(5).is_zero()')
        self.assertFalse(self.frac5.is_zero(), 'Fraction(-50, 125).is_zero()')
        self.assertFalse(self.frac4.is_zero(), 'Fraction(-9, -81).is_zero()')
        self.assertFalse(self.frac6.is_zero(), 'Fraction(3, -8).is_zero()')

    def test_fraction_is_integer(self):
        """
        test if the value of the fraction is an integer
        """
        self.assertTrue(self.frac1.is_integer(), 'Fraction().is_integer()')
        self.assertTrue(self.frac2.is_integer(), 'Fraction(5).is_integer()')
        self.assertTrue(self.frac3.is_integer(), 'Fraction(den=9).is_integer()')

        self.assertFalse(self.frac5.is_integer(), 'Fraction(-50, 125).is_integer()')
        self.assertFalse(self.frac4.is_integer(), 'Fraction(-9, -81).is_integer()')
        self.assertFalse(self.frac6.is_integer(), 'Fraction(3, -8).is_integer()')

    def test_fraction_is_proper(self):
        """
        Test if the value of the fraction is proper
        """
        self.assertTrue(self.frac1.is_proper(), 'Fraction().is_proper()')
        self.assertTrue(self.frac3.is_proper(), 'Fraction(den=9).is_proper()')
        self.assertTrue(self.frac4.is_proper(), 'Fraction(-9, -81).is_proper()')
        self.assertTrue(self.frac6.is_proper(), 'Fraction(3, -8).is_proper()')
        self.assertTrue(self.frac5.is_proper(), 'Fraction(-50, 125).is_proper()')

        self.assertFalse(self.frac2.is_proper(), 'Fraction(5).is_proper()')

    def test_fraction_is_unit(self):
        """
        test if the value of the fraction is unit
        """
        self.assertTrue(self.frac4.is_unit(), 'Fraction(-9, -81).is_unit()')

        self.assertFalse(self.frac1.is_unit(), 'Fraction().is_unit()')
        self.assertFalse(self.frac2.is_unit(), 'Fraction(5).is_unit()')
        self.assertFalse(self.frac3.is_unit(), 'Fraction(den=9).is_unit()')
        self.assertFalse(self.frac5.is_unit(), 'Fraction(-50, 125).is_unit()')
        self.assertFalse(self.frac6.is_unit(), 'Fraction(3, -8).is_unit()')

    def test_fraction_is_adjacent_to(self):
        """
        test if the fraction is adjacent to another fraction
        """
        self.assertFalse(self.frac6.is_adjacent_to(self.frac4), 'Fraction(3, -8).is_adjacent_to(Fraction(-9, -81))')
        self.assertFalse(self.frac4.is_adjacent_to(self.frac6), 'Fraction(-9, -81).is_adjacent_to(Fraction(3, -8))')
        self.assertFalse(self.frac2.is_adjacent_to(self.frac3), 'Fraction(5).is_adjacent_to(Fraction(den=9))')
        self.assertFalse(self.frac1.is_adjacent_to(self.frac5), 'Fraction().is_adjacent_to(Fraction(-50, 125))')


if __name__ == '__main__':
    unittest.main()
