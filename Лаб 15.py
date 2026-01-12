'''
s = 'abcdefg'
print(s[0] + s[2] + s[4] + s[6])
'''

'''
s = 'abcdefg'
print(s[0] * 3 + s[-1] * 3 + s[3] * 2 + s[3] * 2)
'''

'''
s = 'abcdef'
for i in range(len(s)):
    print(s[i])
'''

'''
s = 'abcdef'
for i in s:
    print(i)
'''

'''
s = '01234567891011121314151617'
for i in range(0, len(s), 5):
    print(s[i], end = '')
'''

'''
s = input()
for i in range(0, len(s), 2):
    print(s[i])
'''

'''
s = input()
for i in range(1, len(s) + 1):
    print(s[-i])
'''

'''
s = input()
s1 = input()
s2 = input()
print(s[0] + s1[0] + s2[0])
'''

'''
a = input()
b = 0
for c in a:
    b += int(c)
print(b)
'''

'''
a = input()
flag = False
for c in a:
    if c in '0123456789':
        flag = True
if flag == True:
    print('Цифра')
else:
    print('Цифр нет')
'''