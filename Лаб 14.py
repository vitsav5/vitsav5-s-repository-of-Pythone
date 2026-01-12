'''
a = int(input())
for i in range(1, a + 1):
    for j in range(1, i + 1):
        print(j, end = '')
    print('')
'''

'''
a = int(input())
b = 0
for i in range(1, a + 1):
    for j in range(1, i + 1):
        b += 1
        print(b, end = ' ')
    print('')
'''

'''
a = int(input())
c = 1
flag = True
b = a - 1
b += a
d = 0
for i in range(1, b + 1):
    b = c - 1
    b += c
    d += 1
    while c != 0:
        if c == a:
            flag = False
        if flag == True:
            print(c, end = '')
            c += 1
        else:
            print(c, end = '')
            c -= 1
print('')
'''

'''
a = 0
for i in range(1, 65):
    for j in range(1, 65):
        if 12 * i + 13 * j == 777:
            a += 1
            print('x =', i, 'y =', j)
print(a)
'''

'''
sh = int(input())
v = int(input())
for i in range(v):
    for i in range(sh):
        print('*', end = ' ')
    print('')
'''

'''
a = int(input())
for i in range(a):
    for i in range(1, a + 1):
        print(i, end = ' ')
    print('')
'''

'''
for i in range(1, 11):
    for j in range(1, 11):
        print(f'{j * i : 4}', end = ' ')
    print('')
'''

'''
a = int(input())
b = int(input())
for i in range(1, a):
    for j in range(1, b):
        if 4 * i + 7 * j == 100:
            a += 1
            print('x =', i, 'y =', j)
print(a)
'''