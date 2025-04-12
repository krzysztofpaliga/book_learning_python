f = open('data.txt', 'w')
#
f.write('Hello\n')
#
# 6
f.write('world!\n')
#
# 7
f.close()
#
f = open('data.txt')
#
text = f.read()
#
text
#
# 'Hello\nworld!\n'
print(text)
#
# Hello
# world!
text.split()
#
# ['Hello', 'world!']
for line in open('data.txt')
#
for line in open('data.txt'):
	print(line.rstrip())

#
# Hello
# world!
bf = open('data.bin', 'wb')
#
bf.write(b'h\xFFa\xEEc\xDDk\n')
#
# 8
bf.close()
#
open('data.bin', 'rb').read()
#
# b'h\xffa\xeec\xddk\n'
tf = open('unidata.txt', 'w', encoding='utf-8')
#
tf.write('h\u00c4ck')
#
# 4
tf.close()
#
open('unidata.txt', 'r', encoding='utf-8').read()
#
# 'hÄck'
open('unidata.txt', 'rb').read()
#
# b'h\xc3\x84ck'
'hAck'.encode('utf-8')
#
# b'hAck'
b'h\xc3\x84ck'.decode('utf-8')
#
# 'hÄck'
