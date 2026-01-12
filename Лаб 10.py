'''
i = 0
while i < 10:
    print('Привет')
    i += 1
'''
#Первая команда полностью равна второй
'''
for i in range(10):
    print('Привет')
'''

'''
num = int(input())
while num != -1:
    print('Квадрат вашего числа равен:', num * num)
    num = int(input())
'''

'''
text = input()
total = 0
while text != 'Stop':
    num = int(text)
    total += num
    text = input()
print('Сумма чисел равна', total)
'''

'''
a = input()
if a != 'КОНЕЦ':
    print(a)
while a != 'КОНЕЦ':
    a = input()
    if a != 'КОНЕЦ':
        print(a)
'''

'''
a = input()
if a != 'КОНЕЦ' and a != 'конец':
    print(a)
while a != 'КОНЕЦ' and a != 'конец':
    a = input()
    if a != 'КОНЕЦ' and a != 'конец':
        print(a)
'''

'''
a = input()
b = 0
if a != 'стоп' and a != 'хватит' and a != 'достаточно':
    b += 1
while a != 'стоп' and a != 'хватит' and a != 'достаточно':
    a = input()
    if a != 'стоп' and a != 'хватит' and a != 'достаточно':
        b += 1
print(b)
'''

'''
a = 1
b = 0
c = 1
while a >= 0:
    a = int(input())
    if a >= 0:
        b += a
        c *= a
print(b)
print(c)
'''

'''
a = int(input())
b = 0
while a != 0:
    if a >= 25:
        c = a // 25
        a %= 25
        b += c
    if a >= 10 and a < 25:
        c = a // 10
        a %= 10
        b += c
    if a >= 5 and a < 10:
        c = a // 5
        a %= 5
        b += c
    if a >= 1 and a < 5:
        c = a // 1
        a %= 1
        b += c
print(b)
'''