'''
for i in range(5):
    num = int(input())
    print('Квадрат вашего числа равен:', num * num)
print('Цикл завершён')
'''

'''
for i in range(10):
    print('Python is awesome')
'''

'''
for i in range(5):
    print('AAA')
for j in range(5):
    print('BBBB')
print('E')
for k in range(6):
    print('TTTTT')
print('G')
'''

'''
a = input()
b = int(input())
for i in range(b):
    print(a)
'''

'''
a = int(input())
if 1 <= a <= 20:
    for i in range(a):
        print('**', '**', '**', '**', '**', '**', '*', sep = '*')
else:
    print('Данное число не подходит')
'''

'''
for a in range(10):
    print(a)
print('')
for b in range(1, 10):
    print(b)
print('')
for c in range(3, 7):
    print(c)
print('')
for d in range(7,3):
    print(d)
print('')
for e in range(2, 15, 3):
    print(e)
print('')
for f in range(9, 2, -1):
    print(f)
print('')
for g in range(3, 10, -2):
    print(g)
print('')
'''

'''
a = int(input())
b = int(input())
if a > b:
    print('число a должно быть < числа b')
else:
    print(a)
    for i in range(a, b):
        print(i + 1)
'''

'''
a = int(input())
b = int(input())
if a < b:
    for i in range(a, b + 1):
        print(i)
elif a > b:
    for i in range(a, b - 1, -1):
        print(i)
elif a == b:
    print(a)
'''

'''
a = int(input())
b = int(input())
c = a % 2
d = b % 2
if a >= b:
    if c == 0 and d == 0:
        for i in range(a - 1, b - 1, -2):
            print(i)
    elif c == 0 and d != 0:
        for i in range(a - 1, b - 2, -2):
            print(i)
    elif c != 0 and d == 0:
        for i in range(a, b - 1, -2):
            print(i)
    elif c != 0 and d != 0:
        for i in range(a, b - 2, -2):
            print(i)
else:
    print('Число a должно быть > числа b')
'''

'''
a = int(input())
if 1 <= a <= 10:
    for i in range(1, 11):
        print(a, '*', i, '=', a * i)
'''

'''
a = int(input())
b = int(input())
if a <= b:
    for i in range(a, b + 1):
        c = i % 1717
        if c == 0:
            print(i)
    for i in range(a, b + 1):
        c = i % 100
        if c == 99:
            print(i)
    for i in range(a, b + 1):
        c = i % 33
        d = i % 35
        if c == 0 and d == 0:
            print(i)
else:
    print('Число a должно быть <= числа b')
'''