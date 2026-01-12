'''

      ФУНКЦИИ

def название_функции(условие):
    код

def draw_box():
    for i in range(5):
        print('*' * 7)
draw_box()
print()
draw_box()
print()
draw_box()

def draw_box(height, width):
    for i in range(height):
        print('*' * width)
draw_box(5, 7)
print()
draw_box(4, 4)
print()
draw_box(3, 9)

m = 9  Глобальная переменная
n = 3  Глобальная переменная
def draw_box(height, width):
    for i in range(height):
        print('*' * width)
draw_box(5, 7)
print()
draw_box(4, 4)
print()
draw_box(n, m)

def draw_box(height, width):
    m = 9  Локальная переменная
    n = 3  Локальная переменная
    for i in range(height):
        print('*' * width)
draw_box(5, 7)
print()
draw_box(4, 4)
print()
draw_box(n, m)

Локальные переменные можно использовать только в функции в которой вы их задали
Глобальные переменные можно использовать и в самом коде и в любой функции
'''

'''
def t(temp):
    f = (5 / 9) * (temp - 32)
    return f
temp = float(input('Введите количество градусов по фаренгейту: '))
c = t(temp)
print(c)
'''

'''
def mar(m):
    if m >= 90:
        return 5
    elif m <= 80:
        return 4
    elif m <= 70:
        return 3
    elif m <= 60:
        return 2
    else:
        return 1
m = int(input('Введите вашу отметку по 100-балльной систеье: '))
print(mar(m))
'''

'''
def mar():
    return 10
    return 20

print(mar())
'''

'''
def nums(a, b, c):
    mx = max(a, b, c)
    mn = min(a, b, c)
    mid = a + b + c - mx - mn
    return mid

print(nums(4, 7, 2))
'''

'''
def nums(a, b):
    c = (a ** 2 + b ** 2) ** 0.5
    return c
print(nums(3, 4))
print(nums(5, 12))
print(nums(1, 1))

a = int(input())
b = int(input())
def nums(a, b):
    c = (a ** 2 + b ** 2) ** 0.5
    return c
print(nums(a, b))

def dis(x1, x2, y1, y2):
    return nums(x1 - x2, y1 - y2)
x1, x2 = float(input()), float(input())
y1, y2 = float(input()), float(input())
print(dis(x1, x2, y1, y2))
'''

'''
def sum(a):
    b = 0
    while a > 0:
        b += a % 10
        a //= 10
    return b
a = int(input())
print(sum(a))
'''

'''
def sum(a, b):
    c = max(b)
    c1 = b.index(c)
    return a[c1]
print(sum(['dasf', 'sdfgfdgfsg', 'dsfg', 'fdghfdgh', 'g'], [1.75], [1.61], [1.65], [1.83], [1.64],))
'''