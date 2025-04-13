import math
#
math.pi, math.e
#
# (3.141592653589793, 2.718281828459045)
math.sin(2 * math.pi / 180)
#
# 0.03489949670250097
math.sqrt(144), math.sqrt(2)
#
# (12.0, 1.4142135623730951)
pow(2, 4), 2 ** 4, 2.0 ** 4.0
#
# (16, 16, 16.0)
abs(-62,0), sum((1, 2, 3, 4))
#
abs(-62.0), sum((1, 2, 3, 4))
#
# (62.0, 10)
min(3, 1, 2, 4), max(3, 1, 2, 4)
#
# (1, 4)
math.floor(2.567), math.floor(-2.567)
#
# (2, -3)
math.trunc(2.567), math.trunc(-2.567)
#
# (2, -2)
.567
#
# 0.567
int(2.567), int(-2.567)
#
# (2, -2)
round(2.567), round(2.567, 2), round(2567, -3)
#
# (3, 2.57, 3000)
'%.1f' % 2.567, '{0:.2f}.format(2.567)
#
'%.1f' % 2.567, '{0:.2f}'.format(2.567)
#
# ('2.6', '2.57')
(1 / 3.0), round(1 / 3.0, 2), f'{(1 / 3.0):.2f}'
#
# (0.3333333333333333, 0.33, '0.33')
import math
#
math.sqrt(144)
#
# 12.0
144 ** .5
#
# 12.0
pow(144, .5)
#
# 12.0
import statistics
#
statistics.mean([1, 2, 4, 5, 7])
#
# 3.8
statistics.median([1, 2, 4, 5, 7])
#
# 4
import random
#
ranodm.random()
#
random.random()
#
# 0.6951100242286572
random.random()
#
# 0.8814080606680607
random.randint(1, 10)
#
# 8
random.randint(1, 10)
#
# 9
random.choice(['Pizza', 'Tacos', 'Tikka', 'Lasagna'])
#
# 'Lasagna'
random.choice(['Pizza', 'Tacos', 'Tikka', 'Lasagna'])
#
# 'Tikka'
suits = ['hearts', 'clubs', 'diamonds', 'spades'])
#
suits = ['hearts', 'clubs', 'diamonds', 'spades']
#
random.shuffle(suits)
#
suits
#
# ['diamonds', 'clubs', 'hearts', 'spades']
random.shuffle(suits)
#
suits
#
# ['spades', 'clubs', 'hearts', 'diamonds']
