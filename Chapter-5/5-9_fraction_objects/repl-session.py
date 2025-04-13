from fractions import Fraction
#
x = Fraction(1, 3)
#
y = Fraction(4, 6)
#
x
#
# Fraction(1, 3)
y
#
# Fraction(2, 3)
print(y)
#
# 2/3
x + y
#
# Fraction(1, 1)
x - y
#
# Fraction(-1, 3)
x * y
#
# Fraction(2, 9)
Fraction('.25')
#
# Fraction(1, 4)
Fraction('1.25')
#
# Fraction(5, 4)
Fraction('.25') + Fraction('1.25')
#
# Fraction(3, 2)
a = 1 / 3
#
b = 4 / 6
#
a 
#
# 0.3333333333333333
b
#
# 0.6666666666666666
a + b
#
# 1.0
a - b
#
# -0.3333333333333333
a * b
#
# 0.2222222222222222
0.1 + 0.1 + 0.1 - 0.3
#
# 5.551115123125783e-17
from fractions import Fraction
#
Fraction(1, 10) + Fraction(1, 10) + Fraction(1, 10) - Fraction(3, 10)
#
# Fraction(0, 1)
from decimal import Decimal
#
Decimal('0.1') + Decima('0.1') + Decimal('0.1') - Decimal('0.3')
#
Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3')
#
# Decimal('0.0')
1 / 3
#
# 0.3333333333333333
Fraction(1, 3)
#
# Fraction(1, 3)
import decimal
#
decimal.getcontext().prec = 2
#
Decimal(1) / Decimal(3)
#
# Decimal('0.33')
(1 / 3) + (6 / 12)
#
# 0.8333333333333333
Fraction(1, 3) + Fraction(6, 12)
#
# Fraction(5, 6)
decimal.Decimal(1 / 3) + decimal.Decimal(6 / 12)
#
# Decimal('0.83')
