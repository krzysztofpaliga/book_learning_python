L = [1, 2, 3]
#
M = L
#
L == M
#
# True
L is M
#
# True
M = [1, 2, 3]
#
L == M
#
# True
L is M
#
# False
X = 99
#
Y = 99
#
X == Y
#
# True
X is Y
#
# True
import sys
#
sys.getrefcount(99)
#
# 1000000006
sys.getrefcount(2 ** 1000)
#
# 1
id(99) == id(99)
#
# True
id(99)
#
# 10872520
id(X)
#
# 10872520
id(Y)
#
# 10872520
