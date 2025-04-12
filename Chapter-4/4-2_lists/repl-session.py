L = [123, 'text', 1.23]
#
len(L)
#
# 3
L[0]
#
# 123
L[:-1]
#
# [123, 'text']
L + [4, 5, 6]
#
# [123, 'text', 1.23, 4, 5, 6]
L * 2
#
# [123, 'text', 1.23, 123, 'text', 1.23]
L
#
# [123, 'text', 1.23]
L.append('Py')
#
L
#
# [123, 'text', 1.23, 'Py']
L.pop(2)
#
# 1.23
L
#
# [123, 'text', 'Py']
M = ['bb', 'aa', 'cc']
#
M.sort()
#
M
#
# ['aa', 'bb', 'cc']
M.reverse()
#
M
#
# ['cc', 'bb', 'aa']
L[99]
#
L[99] = 1
#
M = [[1,2,3],
#
	 [4,5,6],
#
     [7,8,9]]
#
M
#
# [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
M[1]
#
# [4, 5, 6]
M[1][2]
#
# 6
col2 = [row[1] for row in M]
#
col2
#
# [2, 5, 8]
[row[1] + 1 for row in M]
#
# [3, 6, 9]
[row[1] for row in M if row[1] % 2 == 0]
#
# [2, 8]
diag = [M[i][i] for i in [0, 1, 2]]
#
diag
#
# [1, 5, 9]
doubles = [c * 2 for c in 'hack']
#
doubles
#
# ['hh', 'aa', 'cc', 'kk']
list(range(4))
#
# [0, 1, 2, 3]
list(range(-6,7,2))
#
# [-6, -4, -2, 0, 2, 4, 6]
[[x ** 2, x ** 3] for x in range(4)]
#
# [[0, 0], [1, 1], [4, 8], [9, 27]]
[[x, x // 2, x * 2] for x in range(-6, 7, 2) if x > 0]
#
# [[2, 1, 4], [4, 2, 8], [6, 3, 12]]
M
#
# [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
G = (sum(row) for row in M)
#
next(G
#
)
#
# 6
next(G)
#
# 15
next(G)
#
# 24
next(G)
#
{sum(row) for row in M}
#
# {24, 6, 15}
{i: sum(M[i]) for i in range(3)}
#
# {0: 6, 1: 15, 2: 24}
