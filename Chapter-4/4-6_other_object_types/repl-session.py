X = set('hack')
#
Y = {'a', 'p', 'p'{
#
Y = {'a', 'p', 'p'}
#
X, Y
#
# ({'c', 'h', 'k', 'a'}, {'p', 'a'})
X & Y, X | Y
#
# ({'a'}, {'p', 'k', 'c', 'h', 'a'})
X - Y, X > Y
#
# ({'c', 'h', 'k'}, False)
list(set([3, 1, 2, 1, 3, 1]))
#
# [1, 2, 3]
set('code') = set('hack')
#
set('code') - set('hack')
#
# {'e', 'd', 'o'}
set('code') == set('deoc')
#
# True
1 > 2, 1 < 2
#
# (False, True)
bool('hack')
#
# True
X = None
#
print(X)
#
# None
L = [None] * 100
#
L
#
# [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
L = [1, 2, 3]
#
type(L)
#
# <class 'list'>
type(type(L))
#
# <class 'type'>
L = 1, 2, 3
#
type(L)
#
# <class 'tuple'>
L = {1, 2, 3}
#
type(L)
#
# <class 'set'>
L = {'a': 1, 'b': 2}
#
type(L)
#
# <class 'dict'>
L = [1, 2, 3]
#
type(L) == type([])
#
# True
type(L) == list
#
# True
isinstance(L, list)
#
# True
x: int = 1
#
x = 'anything'
#
