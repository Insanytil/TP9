import math


class Fraction:
    """Class representing a fraction and operations on it

    Author : L. VERVAEREN
    Date : December 2023
    This class allows fraction manipulations through several operations.
    """

    def __init__(self, num: int = 0, den: int = 1):
        """This builds a fraction based on some numerator and denominator.

        PRE : - numerator (num): must be intµ
              - denominator (den): must be non-null int
        POST : set the two following attributes : 
                - numerator : set as the reduced numerator of the fraction
                - denomitator : set as the reduced denominator of the fraction
        RAISES : - ZeroDivisionError: denominator is null
        """
        if den == 0:
            raise ZeroDivisionError('The denominator can not be null.')
       
        absolute_num = abs(num)
        if num / den > 0:
            num = absolute_num
        else:
            num = -absolute_num
        
        g_common_div = math.gcd(num, den)
        self.__num = num // g_common_div
        self.__den = abs(den) // g_common_div

    @property
    def numerator(self) -> int:
        """
        Get the num of the fraction
        PRE: -
        POST : Return the numerator of the fraction

        """
        return self.__num

    @property
    def denominator(self) -> int:
        """
        Get the denominator of the fraction
        PRE : -
        POST : return denominator of the fraction

        """
        return self.__den

# ------------------ Textual representations ------------------

    def __str__(self) -> str:
        """Return a textual representation of the reduced form of the fraction

        PRE : -
        POST : return '[num / den]'
        """
        return f'[{self.numerator}/{self.denominator}]'
    
    def __repr__(self) -> str:
        """
        Return a textual representation of the reduce form of the fraction
        PRE : -
        POST : return the classname, the numerator and the denomiator as '<Fraction : [num/den]>'

        """
        return str(f"<Fraction: {str(self)}>")

    def as_mixed_number(self):
        """Return a textual representation of the reduced form of the fraction as a mixed number

        A mixed number is the sum of an integer and a proper fraction

        PRE : -
        POST : return the fraction as a mixed number (the sum of the integer part and the fraction part)

        """
        int_part = self.numerator // self.denominator
        frac_part = Fraction(self.numerator % self.denominator, self.denominator)
        return f'{int_part} + {frac_part}'
        
# ------------------ Static method --------------------------
    @staticmethod
    def __set_fraction_param(other):
        """
        verify if another value is an integer or a fraction, then transform it in a fraction
        PRE: - other int or fraction
        POST : return the fractionated value of other
        RAISES : - ValueError : other is not an integer or a fraction

        
        """
        if isinstance(other, int):
            other = Fraction(other)
        
        if not isinstance(other, Fraction):
            raise ValueError('parameter is nor an integer or fraction')
        
        return other
    
# ------------------ Operators overloading ------------------

    def __add__(self, other):
        """Overloading of the + operator for fractions

         PRE : - other : int or fraction
         POST : return  fraction that sums the current fraction and the other fraction
         """
        other = self.__set_fraction_param(other)
        numerator = self.numerator * other.denominator + other.numerator * self.denominator
        denominator = self.denominator * other.denominator
        return Fraction(numerator, denominator)

    def __sub__(self, other):
        """Overloading of the - operator for fractions

        PRE : - other must be int or fraction
        POST : return  fraction that subtracts the current fraction and the other fraction
        RAISES : - ValueError: other is not int or not fraction

        """
        other = self.__set_fraction_param(other)
        numerator = self.numerator * other.denominator - other.numerator * self.denominator
        denominator = self.denominator * other.denominator
        return Fraction(numerator, denominator)

    def __mul__(self, other):
        """Overloading of the * operator for fractions
        PRE : - other: must be an integer or a fraction
        POST : return fraction that multiplies the current fraction and the other fraction
        RAISES : - ValueError: other is not an integer  or not fraction

        """
        other = self.__set_fraction_param(other)

        numerator = self.numerator * other.numerator
        denominator = self.denominator * other.denominator
        return Fraction(numerator, denominator)

    def __truediv__(self, other):
        """Overloading of the / operator for fractions
        PRE : - other: must be an integer or a fraction
        POST : return  fraction that truly divides the current fraction and the other fraction
        RAISES : - ValueError: other is not an integer or not  fraction
        """
        other = self.__set_fraction_param(other)

        numerator = self.numerator * other.denominator
        denominator = self.denominator * other.numerator
        return Fraction(numerator, denominator)

    def __pow__(self, other: int):
        """Overloading of the ** operator for fractions
        PRE : - other: must be integer
        POST : - the current fraction powered by another integer
        """
        if other != 0 and self.is_zero():
            return Fraction()

        numerator = self.numerator
        denominator = self.denominator
        
        if other < 0:
            numerator, denominator = denominator, numerator
            other *= -1

        numerator **= other
        denominator **= other
        return Fraction(numerator, denominator)
    
    def __eq__(self, other) -> bool: 
        """Overloading of the == operator for fractions
        
         PRE : - other: a fraction, an integer or a float
        POST : the equality between the current fraction and the other value (bool)
        """
        return float(self) == float(other)
        
    def __float__(self) -> float:
        """Returns the decimal value of the fraction
        PRE : -
        POST : return the floated value of the fraction
        """
        return self.numerator / self.denominator
    
    def __abs__(self):
        """Returns the absolute value of the fraction
        PRE : -
        POST : the absolute value of the fraction
        """
        return Fraction(abs(self.numerator), self.denominator)


# ------------------ Properties checking  ------------------

    def is_zero(self) -> bool:
        """Check if a fraction's value is 0
        PRE : -
        POST : the numerator is null
        """
        return not self.numerator

    def is_integer(self) -> bool:
        """Check if a fraction is integer (ex : 8/4, 3, 2/2, ...)

        PRE : -
        POST : the reduced denominator equals 1
        """
        return self.denominator == 1

    def is_proper(self) -> bool:
        """Check if the absolute value of the fraction is < 1
        PRE : -
        POST : the absolute value of the fraction is < 1
        """
        return abs(float(self)) < 1

    def is_unit(self) -> bool:
        """Check if a fraction's numerator is 1 in its reduced form
        PRE : -
        POST : the reduced numerator equals 1
        """
        return self.numerator == 1

    def is_adjacent_to(self, other) -> bool:
        """Check if two fractions differ by a unit fraction

        Two fractions are adjacents if the absolute value of the difference between them is a unit fraction

        PRE : - other: a fraction
        POST : ?
        """
        diff = abs(self - other)
        return diff.is_unit()
