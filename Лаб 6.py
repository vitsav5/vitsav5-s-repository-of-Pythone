'''
grade = int(input())
if grade >= 90:
    print('5')
else:
    if grade >= 80:
        print('4')
    else:
        if grade >= 70:
            print('3')
        else:
            if grade >= 60:
                print('2')
            else:
                print('1')
'''

#Это две одинаковые команды но вторая выглядит более презинтабельно

'''
grade = int(input())
if grade >= 90:
    print('5')
elif grade >= 80:
    print('4')
elif grade >= 70:
    print('3')
elif grade >= 60:
    print('2')
else:
    print('1')
'''

'''
a = int(input())
b = int(input())
c = int(input())
if a == b and b == c and c == a:
    print('3')
elif a == b and b != c and c != a:
    print('2')
elif a != b and b == c and c != a:
    print('2')
elif a == c and b != c and b != a:
    print('2')
else:
    print("0")
'''

'''
a = int(input())
b = int(input())
c = int(input())
if a > b > c or c > b > a:
    print(b)
elif b > a > c or c > a > b:
    print(a)
elif b > c > a or a > c > b:
    print(c)
'''

'''
a = int(input())
if a > 69:
    print('К сожалению вы не проходите условия саревнования')
elif 69 >= a > 64:
    print('Полусредний вес')
elif 64 >= a > 60:
    print('Первый полусредний вес')
elif 60 >= a > 50:
    print('Лёгкий вес')
elif a < 50:
    print('К сожалению вы не проходите условия саревнования')
'''

'''
a = input()
b = input()
if a == 'Красный' and b == 'Синий':
    print('Фиолетовый')
elif a == 'Красный' and b == 'Жёлтый':
    print('Оранжевый')
elif a == 'Жёлтый' and b == 'Синий':
    print('Зелёный')
else:
    print('Ошибка')
'''

'''
a = input()
b = input()
c = input()
d = input()
e = input()
f = input()
g = input()
print('Больше всего мне понравилось', a)
print('Я почти переварил', b)
print('Мне не понравилась', c)
print('Я рекомендую', d)
print('Я переел', e)
print('Я съел бы ещё чуть чуть', f)
print('Сейчас я себя чувствую', g)
'''