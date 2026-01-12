'''
Сегодня мы изучаем
and
or
not
'''

#AND

'''
age = int(input())
grade = int(input())
city = input()
if age >= 12 and grade >= 7 and city == 'Москва':
    print('Доступ разрещён.')
else:
    print('Доступ запрещён.')
'''

#Можно писать сразу несколько and

#OR

'''
city = input()
if city == 'Москва' or city == 'Уфа': 
    print('Доступ разрещён.')
else:
    print('Доступ запрещён.')
'''

#Можно писать сразу несколько or

#Также в одной команде можно писать и and и or

'''
age = int(input())
grade = int(input())
city = input()
if age >= 12 and grade >= 7 and city == 'Москва' or city == 'Уфа' or city == 'Тула':
    print('Доступ разрещён.')
else:
    print('Доступ запрещён.')
'''

'''
age = int(input())
if not (age < 12):
    print('Доступ разрещён.')
else:
    print('Доступ запрещён.')
'''

'''
a = int(input())
b = a // 100
if b > 0 and b <= 9:
    print(a, '-- трёхзначное число')
else:
    print(a, '-- не трёхзначное число')
'''

'''
a = int(input())
b = a % 10
c = (a // 10) % 10
d = a // 100
if b == c and c == d and d == b:
    print('Число', a, 'состоит из одной и той же цифры')
else:
    print('Число', a, 'состоит из разных цифр')
'''

'''
a = int(input())
b = int(input())
if a > 0 and b > 0:
    print('Точка находиться в 1 четверти')
if a < 0 and b > 0:
    print('Точка находиться в 2 четверти')
if a < 0 and b < 0:
    print('Точка находиться в 3 четверти')
if a > 0 and b < 0:
    print('Точка находиться в 4 четверти')
'''

'''
a = int(input())
b = 0
if a > -30 and a <= -2:
    b = b + 1
if a > 7 and a <= 25:
    b = b + 1
if b == 1:
    print('YES')
else:
    print('NO')
'''

'''
a = int(input())
b = a % 4
if b == 0:
    print('YES')
else:
    print('NO')
'''