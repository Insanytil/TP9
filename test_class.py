from fraction import Fraction

if __name__ == '__main__':
    print('--- TEST : FRACTION CLASS ---\n')
    try:
        print('Fraction(5,0) :', end=' ')
        print(Fraction(5, 0))
    except ZeroDivisionError as error:
        print(error)

    fraction1 = Fraction(-50, 125)
    print(f'Fraction(-50, 125) : {fraction1} ; {fraction1.as_mixed_number()}')
    fraction2 = Fraction(-9, -81)
    print(f'Fraction(-9, -81) : {fraction2} ; {fraction2.as_mixed_number()}')
    fraction3 = Fraction(3, -8)
    print(f'Fraction(3, -8) : {fraction3} ; {fraction3.as_mixed_number()}')

    num_frac1 = int(input('Numerator Fraction 1: '))
    den_frac1 = int(input('Denominator Fraction 1: '))
    num_frac2 = int(input('Numerator Fraction 2: '))
    den_frac2 = int(input('Denominator Fraction 2: '))

    frac1 = Fraction(num_frac1, den_frac1)
    print(f"Fraction 1 : {frac1} ; {frac1.as_mixed_number()}")
    frac2 = Fraction(num_frac2, den_frac2)
    print(f"Fraction 2 : {frac2} ; {frac2.as_mixed_number()}\n")

    print(f"{frac1} + {frac2} = {frac1 + frac2}")
    print(f"{frac1} - {frac2} = {frac1 - frac2}")
    print(f"{frac1} * {frac2} = {frac1 * frac2}")
    print(f"{frac1} / {frac2} = {frac1 / frac2}")
    print(f"{frac1} ** 3 = {frac1 ** 3}")
    print(f"{frac2} ** 4 = {frac2 ** 4}\n")

    print(f"float({frac1}) = {abs(frac1)}")
    print(f"float({frac2}) = {abs(frac2)}\n")

    print(f"abs({frac1}) = {abs(frac1)}")
    print(f"abs({frac2}) = {abs(frac2)}\n")

    print(f"{frac1} = {frac2} : {frac1 == frac2}")

    print(f"Is {frac1} zero ? : {frac1.is_zero()}")
    print(f"Is {frac2} zero ? : {frac2.is_zero()}")
    print(f"Is {frac1} an integer ? : {frac1.is_integer()}")
    print(f"Is {frac2} an integer ? : {frac2.is_integer()}")
    print(f"Is {frac1} proper ? : {frac1.is_proper()}")
    print(f"Is {frac2} proper ? : {frac2.is_proper()}")
    print(f"Is {frac1} unit ? : {frac1.is_unit()}")
    print(f"Is {frac2} unit ? : {frac2.is_unit()}")
    print(f"Is {frac1} and {frac2} adjacents ? : {frac1.is_adjacent_to(frac2)}\n")
