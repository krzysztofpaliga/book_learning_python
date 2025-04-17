'62' + 1
#
int('62'), str(62)
#
# (62, '62')
S = '62'
#
I = 1
#
S + I
#
int(S) + I
#
# 63
S + str(I)
#
# '621'
float('1.5') + 2.8
#
# 4.3
'1.5' + str(2.8)
#
# '1.52.8'
ord('h')
#
# 104
chr(104)
#
# 'h'
for c in 'hack':
	print(c, ord(c))

#
# h 104
# a 97
# c 99
# k 107
S = '5'
#
S = chr(ord(S) + 1)
#
S
#
# '6'
S = chr(ord(S) + 1)
#
S
#
# '7'
int('5')
#
# 5
ord('5') - ord('1')
#
# 4
'hack' == 'hack', 'hack' > 'hack', 'hackt' > 'hack', 'hacker' > 'hack'
#
# (True, False, True, True)
