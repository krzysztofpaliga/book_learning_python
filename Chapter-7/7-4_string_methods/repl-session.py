S = 'textly!'
#
S[:4] + 'ful' + S[-1]
#
# 'textful!'
S.replace('ly', 'ful')
#
# 'textful!'
'--@--@--@--'.replace('@', 'PY', 2)
#
# '--PY--PY--@--'
'--@--@--@--'.replace('@', 'PY', 2).replace('--', '||')
#
# '||PY||PY||@||'
S = 'text'
#
L = list(S)
#
L
#
# ['t', 'e', 'x', 't']
L[0] = 'h'
#
L[3] = '!'
#
L
#
# ['h', 'e', 'x', '!']
S = ''.join(L)
#
S
#
# 'hex!'
'PY'.joind(['which', 'languge', 'is', 'best', '?'])
#
'PY'.join(['which', 'languge', 'is', 'best', '?'])
#
# 'whichPYlangugePYisPYbestPY?'
line = 'Python\'s strings are awesome!\n'
#
line.rstrip()
#
# "Python's strings are awesome!"
line.upper()
#
# "PYTHON'S STRINGS ARE AWESOME!\n"
line.isalpha()
#
# False
line.enswith('awesome!
#
line.enswith('awesome!\n')
#
line.endswith('awesome!\n')
#
# True
line.startswith('Python')
#
# True
line.find('awesome') != -1
#
# True
'awesome' in line
#
# True
sub = 'awesome!\n'
#
line.endswith(sub)
#
# True
line[-len(sub):] == sub
#
# True
