'''
def a():
    print('*' * 10)
    for i in range(12):
        print('*', ' ' * 6, '*')
    print('*' * 10)
a()
'''

'''
def a():
    b = 1
    for i in range(10):
        print('* ' * b)
        b += 1
a()
'''

'''
def a(b):
    return b * 0.6214
c = int(input())
print(a(c))
'''

'''
def num(a):
    if (a * 100) % 100 >= 50:
        return int(((a * 100) // 100) + 1)
    else:
        return int((a * 100) // 100)
b = float(input())
print(num(b))
'''

'''
a = []
def nums(c):
    for i in range(1, c + 1):
        if c % i == 0:
            a.append(i)
    print(a)
b =  int(input())
nums(b)
'''

'''
def nums(c):
    num = 0
    for i in range(1, c + 1):
        if c % i == 0:
            num += 1
    print(num)
b = int(input())
nums(b)
'''

'''
def num(a, b, c, d,):
    x1 = (d + c) / 2
    x2 = (a + b) / 2
    print(x1, ';', x2)
a = float(input())
b = float(input())
c = float(input())
d = float(input())
num(a, b, c, d)
'''