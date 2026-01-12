'''
a = int(input())
while a != 0:
    b = a % 10
    print(b)
    print(b + b)
    print(b * b)
    a = a // 10
'''

'''
a = int(input())
b = False
while a != 0:
    c = a % 10
    if c == 7:
        b = True
    a = a // 10
if b == True:
    print('Yes')
else:
    print('No')
'''

'''
a = 12345
b = 1
while a != 0:
    c = a % 10
    b = b * c
    a = a // 10
print(b)
'''

'''
a = 123456789
b = 0
while a != 0:
    c = a % 10
    if c > 4:
        b += 1
    a = a // 10
print(b)
'''

'''
a = int(input())
while a != 0:
    b = a % 10
    print(b)
    a = a // 10
'''

'''
a = int(input())
a1 = a
b = 0
while a1 != 0:
    c = a1 % 10
    b = b + c
    a1 = a1 // 10
print(b)
a2 = a
b1 = 0
while a2 != 0:
    c = a2 % 10
    if c != 0:
        b1 = b1 + 1
    a2 = a2 // 10
print(b1)
a3 = a
b = 1
while a3 != 0:
    c = a3 % 10
    b = b * c
    a3 = a3 // 10
print(b)
a4 = a
b = 1
while a4 != 0:
    c = a4 % 10
    b = b + c
    a4 = a4 // 10
b = b / b1
print(b)
c = 10 ** (b1 - 1)
a5 = a
b = a5 // c
print(b)
a6 = a % 10
b = b + a6
print(b)
'''

'''
a = int(input())
b = True
a1 = a % 10
while a != 0:
    c = a % 10
    if c != a1:
        b = False
    a = a // 10
if b == True:
    print('YES')
else:
    print('NO')
'''