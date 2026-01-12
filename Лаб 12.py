'''
a = 0
for i in range(10):
    b = int(input())
    if b < 0:
        break
    a += b
print(a)
'''

'''
a = int(input())
b = True

for i in range(2, a):
    if a % i == 0:
        b = False
        break
if b == True:
    print('Число простое')
else:
    print('Число составное')
'''

'''
a = int(input())
a1 = a
b = False
while a != 0:
    c = a1 % 10
    if c == 7:
        b = True
        break
    a1 //= 10
if b == True:
    print('Число', a, 'содержит цифру 7')
else:
    print('Число', a, 'не содержит цифру 7')
'''

'''
for i in range(1, 101):
    if i == 7 or i == 17 or i == 29 or i == 78:
        continue
    print(i)
'''

'''
for i in range(10):
    print(i, end='*')
    if i > 6:
        break
'''

'''
a = 0
for i in range(10):
    if i % 2 == 0:
        continue
    a += i
print(a)
'''

'''
a = 1
for i in range(1, 11):
    if i % 2 == 0:
        continue
    if i % 9 == 0:
        break
    a *= i
print(a)
'''

'''
i = 1
while i < 101:
    if i % 7 == 0:
        print(i)
        i += 1
'''

'''
i = 1
while i < 101:
    if i % 7 == 0:
        print(i)
    i += 1
'''

'''
for i in range(7, 101, 7):
    print(i)
'''

'''
for i in range(1, 100):
    print(101 - i)
'''

'''
for i in range(1, 100):
    print(101 - i)
'''

'''
for i in range(100, 0, -1):
    print(i)
'''

'''
a = 1
for i in range(1, 1000):
    if i % 2 == 1:
        a = a + 1
print(a)
'''

'''
a = 0
for i in range(1, 1001):
    if i % 2 == 1:
        a += 1
print(a)
'''

'''
a = int(input())
b = 0
for i in range(a):
    b = b * i
print(a)
'''

'''
a = int(input())
b = 1
for i in range(1, a + 1):
    b *= i
print(a)
'''

'''
a = int(input())
b = 0
c = 0
while a != -1:
    if a >  7:
        b += a
        c += 1
    a = int(input())
print(b / c)
'''

'''
a = int(input())
b = 1
c = 1
while c != 0:
    b += 1
    c = a % b
print(b)
'''