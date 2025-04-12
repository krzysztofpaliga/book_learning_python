s = 'Code'
#
len(s)
#
# 4
s[0]
#
# 'C'
s[1]
#
# 'o'
#
s[-1]
#
# 'e'
s[-2]
#
# 'd'
s[len(s)-1]
#
# 'e'
s
#
# 'Code'
s[1:-1]
#
# 'od'
s[1:-3]
#
# ''
s[1:3]
#
# 'od'
s[1:]
#
# 'ode'
s[:3]
#
# 'Cod'
s[:-1]
#
# 'Cod'
s[:]
#
# 'Code'
s + 'xyz'
#
# 'Codexyz'
s * 8
#
# 'CodeCodeCodeCodeCodeCodeCodeCode'
s[0] = 'z'
#
'z' + s[1:]
#
# 'zode'
S = 'Python'
#
L = list(S)
#
L[0] = 'C'
#
''.join(L)
#
# 'Cython'
B = bytearray(b'app')
#
B.extend(b'lication')
#
B
#
# bytearray(b'application')
#
B.decode()
#
# 'application'
S = 'Code'
#
S.find('od')
#
# 1
S.replace('od', 'abl')
#
# 'Cable'
S
#
# 'Code'
line - 'aaa,bbb,ccccc,dd'
#
line = 'aaa,bbb,ccccc,dd'
#
line.split(',')
#
# ['aaa', 'bbb', 'ccccc', 'dd']
#
S = 'code'
#
S.upper()
#
# 'CODE'
S.isalpha()
#
# True
#
line = 'aaa,bbb,ccccc,dd\n'
#
line.rstrip()
#
# 'aaa,bbb,ccccc,dd'
line.rstrip().split(',')
#
# ['aaa', 'bbb', 'ccccc', 'dd']
line
#
# 'aaa,bbb,ccccc,dd\n'
tool = 'Python'
#
major = 3
#
minor = 3
#
'Using %s version %s.%s' % (tool, major, minor + 9)
#
# 'Using Python version 3.12'
'Using {} version {}.{}'.format(tool, major, minor + 9)
#
# 'Using Python version 3.12'
f'Using {tool} version {major}.{minor + 9}'
#
# 'Using Python version 3.12'
'%.2f | %+05d' % (3.14159, -62)
#
# '3.14 | -0062'
'{1:,.2f} | {0}'.format('sapp'[1:], 296999.256)
#
# '296,999.26 | app'
#
#
#
# '296,999.26 | {"sapp"[1:]}'
f'{296999.256:,.2f} | {"sapp"[1:]}'
#
# '296,999.26 | app'
dir
#
# <built-in function dir>
dir(S)
#
# ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
help(S.replace)
'hÄck'
#
# 'hÄck'
#
b'a\x01c'
#
# b'a\x01c'
'Code'
#
# 'Code'
'Code'.encode('utf-8')
#
# b'Code'
'Code'.encode('utf-16')
#
# b'\xff\xfeC\x00o\x00d\x00e\x00'
ord('a')
#
# 97
hex(ord('a'))
#
# '0x61'
