len('abc')
#
# 3
'abc' + 'def'
#
# 'abcdef'
'Py!' * 4
#
# 'Py!Py!Py!Py!'
myjob = 'hacker'
#
for c in myjob:
' '
	print(c, end=' ')

#
for c in myjob:
	print(c, end=' ')

#
# h a c k e r
'k' in myjob
#
# True
'z' in myjob
#
# False
'HACK' in 'abcHACKdef'
#
# True
'HACK' in 'abcHACdKef'
#
# False
S = 'code'
#
S[0], S[-2]
#
# ('c', 'd')
S[1:3], S[1:], S[:-1]
#
# ('od', 'ode', 'cod')
S = 'code'
#
S[99]
#
S[1:99]
#
# 'ode'
S = 'abcdefghijklmnop'
#
S[1:10:2]
#
# 'bdfhj'
S[::2]
#
# 'acegikmo'
S[::-1]
#
# 'ponmlkjihgfedcba'
S[1:5:-1]
#
# ''
S[5:1:-1]
#
# 'fedc'
S[5:0:-1]
#
# 'fedcb'
'code'[1:3]
#
# 'od'
'code'[slice(1, 3)]
#
# 'od'
'code'[::-1]
#
# 'edoc'
'code'[slice(None, None, -1)]
#
# 'edoc'
