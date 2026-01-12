'''
print('Какой язык програмирования мы изучаем?')
answer = input()
if answer == 'Python':
    print('Верно! Мы ботаем Python =)')
    print('Python - отличный язык!')
else:
    print('Не совсем так!')
'''

'''
num1 = int(input())
num2 = int(input())

if num1 < num2:
    print(num1, 'меньше чем', num2)

if num1  > num2:
    print(num1, 'больше чем', num2)

if num1 == num2:
    print(num1, 'равно', num2)

if num1 != num2:
    print(num1, 'не равно', num2)
'''

'''
age = int(input())
if 3 <= age <= 6:
    print('Вы ребёнок!')

a = int(input())
b = int(input())
c = int(input())
if a == b == c:
    print('Числа равны')
else:
    print('Числа не равны')
'''

'''
answer = input()
if answer == 'Python':
    print('Да!')
else:
    print('Нет!')
'''

'''
number = int(input())
a = number % 10
b = number // 10
if a == b:
    print('Да!')
else:
    print('Нет!')
c = a + b
d = a * b
print('Сумма a и b =', c)
print('Сумма a и b =', d)
'''

'''
a = int(input())
b = int(input())
c = int(input())
d = 0 
if a % 2 == 0:
    d = d + 1
if b % 2 == 0:
    d = d + 1
if a % 2 == 0:
    d = d + 1
print(d)
'''

'''
b = 0
print('Введите пароль')
a = input()
if a == '102':
    b = b + 1
print('Подтвердите пароль')
c = input()
if c == '102':
    b = b + 1
if b == 2:
    print('Пароль принят')
else:
    print('Пароль не принят')
'''

'''
print('Введите ваш возрост')
a = int(input())
if a < 0:
    print('Введите правильное значение')
    a = int(input())
if a >= 18:
    print('Доступ разрешён')
else:
    print('Доступ запрещён')
'''

'''
a = int(input())
b = int(input())
if a == b:
    print(a, '=', b)
if a > b:
    print(b)
else:
    print(a)
'''

'''
a = int(input())
if 0 < a < 13:
    print('Детство')
if 13 < a <18:
    print('Полростковый возрост')
if 18 <= a <= 120:
    print('Зрелость')
if a > 120:
    print('Смерть')
'''