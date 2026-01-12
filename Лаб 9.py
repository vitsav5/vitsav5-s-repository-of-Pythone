'''
Нахождение максимального

a = -1
for i in range(10):
    num = int(input())
    if num > a:
        a = num
print(a)
'''

'''
Нахождение менимального
a = int(input())
for i in range(10):
    num = int(input())
    if num < a:
        a = num
print(a)
'''

'''
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
a = a + 1
b = b + c
d = d - e
print(a, b, d,)

#Всецило и полностью = следующиму

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
a += 1
b += c
d -= e
print(a, b, d,)
'''

'''
a = 0
for i in range(1, 6):
    a += i
    print(a)
'''

'''
!!!!!!!
a = 0
for i in range(10):
    b = int(input())
    if b > 10:
        a = a + 1
print(a)
'''

'''
!!!!!!!
a1 = 0
a2 = 0
for i in range(10):
    num = int(input())
    if num > 10:
        a1 += 1
    if num == 0:
        a2 += 1
print(a1, a2)
'''

'''
!!!!!!!
a = 0
for i in range(10):
    num = int(input())
    if num > 10:
        a = a + num
print(a)
'''

'''
a = 0
for i in range(1, 101):
    a += i
print(a)
'''

'''
a = 0
for i in range(10):
    num = int(input())
    a = a + num
b = a / 10
print(b)
'''

'''
a = 1
for i in range(10):
    num = int(input())
    if num > 10:
        a = a * num
print(a)
'''

'''
num = int(input())
flag = True

for i in range(2, num):
    if num % i == 0:
        flag = False

if flag == True:
    print('Число простое')
else:
    print('Число составное')
'''

'''
a = int(input())
b = int(input())
c = 0
if a <= b:
    for i in range(a, b + 1):
        d = i ** 3
        e = d % 10
        if e == 4 or e == 9:
            c += 1
    print(c)
else:
    print('Число a должно быть меньше числа b')
'''

'''
a = int(input())
b = 0
for i in range(a):
    c = int(input())
    b += c
print(b)
'''

'''
a = int(input())
c = 0
for i in range(1, a + 1):
    d = i ** 2
    e = d % 10
    if e == 2 or e == 5 or e == 8:
        c += i
print(c)
'''

'''
a = int(input())
b = 1
for i in range(1, a + 1):
    b = b * i
print(b)
'''

'''
a = 1
for i in range(10):
    b = int(input())
    if b != 0:
        a = a * b
print(a)
'''