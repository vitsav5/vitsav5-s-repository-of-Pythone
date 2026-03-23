'''
a = int(input('Ваш счёт: '))
if a > 100:
    print('Рекорд!')
'''

'''
import random

secret = random.randint(1, 10)

while True:
    try:
        guess = int(input('Угадай число от 1 до 10: '))

        if guess < secret:
            print('Больше!')
        elif guess > secret:
            print('Меньше!')
        else:
            print('Победа!')
            break  # Выходим из цикла только при победе

    except ValueError:
        print('Ошибка! Введи именно число, а не буквы.')
'''

'''
a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
o = input("Введите операцию (+, -, *, /): ")

if o == '+':
    print(a + b)
elif o == '-':
    print(a - b)
elif o == '*':
    print(a * b)
elif o == '/':
    if b != 0:
        print(a / b)
    else:
        print('Ошибка: деление на ноль')
else:
    print('Неизвестная операция')
'''

'''
import random

def name(n):
    return {1: 'Камень', 2: 'Ножницы', 3: 'Бумага'}.get(n, 'Неизвестно')

def get_player_choice():
    try:
        x = int(input('Введите 1(Камень), 2(Ножницы) или 3(Бумага): ').strip())
    except ValueError:
        print('Неверный ввод. Введите число 1, 2 или 3.')
        return None
    if x not in (1, 2, 3):
        print('Число должно быть 1, 2 или 3.')
        return None
    return x

def decide(player, comp):
    if player == comp:
        return 'Ничья'
    # Правила по вашему описанию:
    # 1 и 3 -> побеждает тот, кто 3 (Бумага побеждает Камень)
    # 1 и 2 -> побеждает тот, кто 1 (Камень побеждает Ножницы)
    # 2 и 3 -> побеждает тот, кто 2 (Ножницы побеждают Бумагу)
    pair = {player, comp}
    if pair == {1, 3}:
        winner = 3
    elif pair == {1, 2}:
        winner = 1
    elif pair == {2, 3}:
        winner = 2
    else:
        return 'Ошибка в логике'
    return 'Игрок выиграл' if player == winner else 'Компьютер выиграл'

def main():
    player = None
    while player is None:
        player = get_player_choice()
    comp = random.randint(1, 3)
    print(f'Игрок: {name(player)}  —  Компьютер: {name(comp)}')
    print(decide(player, comp))

if __name__ == '__main__':
    main()
'''

'''
def calculate_damage(attack, defence, level):
    base = attack * 1.5
    reduction = defence * 0.3
    bonus = level * 2
    final = base - reduction + bonus
    if final < 1:
        final = 1
    return int(final)
'''