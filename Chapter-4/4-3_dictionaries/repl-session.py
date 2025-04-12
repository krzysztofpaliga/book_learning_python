D = {'name': 'Pat', 'job': 'dev', 'age': 40}
#
D['name']
#
# 'Pat'
D['job'] = 'mgr'
#
D
#
# {'name': 'Pat', 'job': 'mgr', 'age': 40}
D = {}
#
D['name'] = 'Pat'
#
D['job'] = 'dev'
#
D['age'] = 40
#
D
#
# {'name': 'Pat', 'job': 'dev', 'age': 40}
pat1 = dict(name='Pat', job='dev', age=40)
#
pat1
#
# {'name': 'Pat', 'job': 'dev', 'age': 40}
pat2 = dict(zip(['name', 'job', 'age'], ['Pat', 'dev', 40]))
#
pat2
#
# {'name': 'Pat', 'job': 'dev', 'age': 40}
rec = {'name': {'first': 'Pat', 'last': 'Smith'},
       #
       'jobs': ['dev', 'mgr'],
       #
       'age': 40.5}
#
rec
#
# {'name': {'first': 'Pat', 'last': 'Smith'}, 'jobs': ['dev', 'mgr'], 'age': 40.5}
rec['name']
#
# {'first': 'Pat', 'last': 'Smith'}
rec['name']['last']
#
# 'Smith'
rec['jobs']
#
# ['dev', 'mgr']
rec['jobs'][-1]
#
# 'mgr'
rec['jobs'].append('janitor')
#
rec
#
# {'name': {'first': 'Pat', 'last': 'Smith'}, 'jobs': ['dev', 'mgr', 'janitor'], 'age': 40.5}
D = {'a': 1, 'b': 2, 'c': 3}
#
D['d'] = 4
#
D
#
# {'a': 1, 'b': 2, 'c': 3, 'd': 4}
D['e']
#
'e' in D
#
# False
if not 'e' in D:
    print('missing key!')

#
# missing key!
#
if not 'e' in D:
    print('missing key!')
    print('no, really...')

#
# missing key!
# no, really...
D
#
# {'a': 1, 'b': 2, 'c': 3, 'd': 4}
D.get('a', 'missing')
#
# 1
D.get('e', 'missing')
#
# 'missing'
D['e'] if 'e' in D else 0
#
# 0
dir(D)
#
# ['__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__ior__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__ror__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
D
#
# {'a': 1, 'b': 2, 'c': 3, 'd': 4}
D.popitem('d')
#
D.popitem()
#
# ('d', 4)
D
#
# {'a': 1, 'b': 2, 'c': 3}
list(D.keys())
#
# ['a', 'b', 'c']
list(D.values())
#
# [1, 2, 3]
list(D.items())
#
# [('a', 1), ('b', 2), ('c', 3)]
D.keys()
#
# dict_keys(['a', 'b', 'c'])
I = iter(D.keys())
#
next(I)
#
# 'a'
next(I)
#
# 'b'
for key in D.keys():
    print(key, '=>', D[key])

#
# a => 1
# b => 2
# c => 3
for key in D:
    print(key, '=>', D[key])

#
# a => 1
# b => 2
# c => 3
for (key, value) in D.items():
    print(key, '=>', value)

#
# a => 1
# b => 2
# c => 3
