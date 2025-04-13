x = set('abcde')
#
x
#
# {'c', 'd', 'e', 'a', 'b'}
y = {99, 'b', 'y', 'd', 1.2}
#
y
#
# {1.2, 99, 'd', 'b', 'y'}
z = set()
#
z
#
# set()
z = set([1.2, 'a', 3, 1.2, 'a'])
#
z
#
# {1.2, 3, 'a'}
{1, *'abc', *[1, 2, 3]}
#
# {1, 2, 3, 'c', 'a', 'b'}
x = set('abcd')
#
y = set('bdxy')
#
x - y
#
# {'a', 'c'}
x | y
#
# {'c', 'd', 'a', 'b', 'y', 'x'}
x & y
#
# {'d', 'b'}
x ^ y
#
# {'c', 'a', 'y', 'x'}
x < y, x > y
#
# (False, False)
'd' in x
#
# True
'd' in 'code', 2 in [1, 2, 3]
#
# (True, True)
dir(x)
#
# ['__and__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__iand__', '__init__', '__init_subclass__', '__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']
x
#
# {'a', 'c', 'd', 'b'}
z
#
# {1.2, 3, 'a'}
z = x.intersection(y)
#
z
#
# {'d', 'b'}
z.add('HACK')
#
z
#
# {'HACK', 'd', 'b'}
z.update(set(['X', 'Y']))
#
z
#
# {'b', 'X', 'Y', 'HACK', 'd'}
z.remove('b')
#
z
#
# {'X', 'Y', 'HACK', 'd'}
for item in set('abc'):
	print(item * 3)

#
# aaa
# ccc
# bbb
{'a', 'b', 'c'} + {'d'}
#
S = set([1, 2, 3])
#
S | set([3, 4])
#
# {1, 2, 3, 4}
S | [3,4]
#
S.union([3,4])
#
# {1, 2, 3, 4}
S.intersection((1, 3, 5))
#
# {1, 3}
S.issubset(range(-5, 5))
#
# True
S 
#
# {1, 2, 3}
S.intersection_update((1, 2, 5))
#
S
#
# {1, 2}
S |= {1, 2, 4}
#
S
#
# {1, 2, 4}
S = {1.23}
#
S.add([1, 2, 3])
#
S.add({'a': 1})
#
S.add((1, 2, 3))
#
S
#
# {1.23, (1, 2, 3)}
S | {(4, 5 ,6), (1, 2, 3)}
#
# {1.23, (1, 2, 3), (4, 5, 6)}
(1, 2, 3) in S
#
# True
(1, 3, 3) in S
#
# False
S.add(frozenset('app'))
#
S
#
# {1.23, (1, 2, 3), frozenset({'a', 'p'})}
{ x ** 2 for x in [1, 2, 3, 4]}
#
# {16, 1, 4, 9}
{x for x in 'py3X'}
#
# {'y', '3', 'X', 'p'}
{c * 4 for c in 'py3X'}
#
# {'XXXX', 'pppp', 'yyyy', '3333'}
{c * 4 for c in 'py3X' + 'py2X'}
#
# {'XXXX', '3333', 'yyyy', 'pppp', '2222'}
S = {c * 4 for c in 'py3X'}
#
S | {'zzzz', 'XXXX'}
#
# {'XXXX', 'pppp', 'zzzz', '3333', 'yyyy'}
S & {'zzzz', 'XXXX'}
#
# {'XXXX'}
L = [1, 2, 1, 3, 2, 4, 5]
#
set(L)
#
# {1, 2, 3, 4, 5}
L = list(set(L))
#
L
#
# [1, 2, 3, 4, 5]
list(set(['yy', 'cc', 'aa', 'xx', 'dd', 'aa']))
#
# ['yy', 'aa', 'dd', 'xx', 'cc']
set([1, 3, 5, 7]) - set([1, 2, 4, 5, 6])
#
# {3, 7}
set('abcdefg') - set('abdghij')
#
# {'f', 'c', 'e'}
set('code') - set(['t', 'o', 'e'])
#
# {'c', 'd'}
L1, L2 = [1, 3, 5, 2, 4], [2, 5, 3, 4, 1]
#
L1 == L2
#
# False
set(L1) == set(L2)
#
# True
sorted(L1) == sorted(L2)
#
# True
'code' == 'edoc', set('code') == set('edoc'), sorted('code') == sorted('edoc')
#
# (False, True, True)
engineers = {'pat', 'ann', 'bob', 'sue'}
#
managers = {'sue', 'tom'}
#
'pat' in engineers
#
# True
engineers & managers
#
# {'sue'}
engineers | managers
#
# {'tom', 'pat', 'ann', 'bob', 'sue'}
engineers - managers
#
# {'pat', 'bob', 'ann'}
managers - engineers
#
# {'tom'}
engineers > managers?
#
engineers > managers
#
# False
{'sue', 'bob'} < engineers
#
# True
(managers | engineers) > managers
#
# True
managers ^ engineers
#
# {'pat', 'bob', 'ann', 'tom'}
