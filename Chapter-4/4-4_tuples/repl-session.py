T = (1, 2, 3, 4)
#
len(T)
#
# 4
T + (5, 6)
#
# (1, 2, 3, 4, 5, 6)
T[0], T[1:]
#
# (1, (2, 3, 4))
T
#
# (1, 2, 3, 4)
(T[0], T[1:])
#
# (1, (2, 3, 4))
T.index(4)
#
# 3
T.count(4)
#
# 1
T[0] = 2
#
T = (2,) + T[1:]
#
T
#
# (2, 2, 3, 4)
T = 'hack', 3.0, [11, 22, 33]
#
T
#
# ('hack', 3.0, [11, 22, 33])
T[1]
#
# 3.0
T[2][1]
#
# 22
T.append(4)
#
