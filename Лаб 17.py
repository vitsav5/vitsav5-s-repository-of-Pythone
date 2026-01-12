'''
s = 'foO BaR BAz qux'
print(s.capitalize())
s = 'FOO  Bar 123 baz qUX'
print(s.swapcase())
s = 'foo bar baz qux'
print(s.title())
s = 'FOO  Bar 123 baz qUX'
print(s.lower())
s = 'FOO  Bar 123 baz qUX'
print(s.upper())

s = 'foo goo moo'
print(s.count('oo'))
s = 'foobar'
print(s.startswith('foo'))
print(s.startswith('baz'))
s = 'foobar'
print(s.endswith('bar'))
print(s.endswith('baz'))
s = '     foo bar foo baz foo qux     '
print(s.find('foo')) # Ищет первое сочетание знаков и выдаёт индекс где они начинаются (если такого нет то выводит -1)
print(s.find('bar'))
print(s.find('qu'))
print(s.find('dbgadtg'))
print(s.strip())
print(s.lstrip())
print(s.rstrip())
print(s.replace('foo', 'sdfagfa')) # Замена чего то на что то
'''

'''
s = input()
s1 = s.title()
if s == s1:
    print('YES')
else:
    print('NO')
'''

'''
s = input()
s1 = s.lower()
a = s1.find('хорош')
if a >= 0:
    print('YES')
else:
    print('NO')
'''

'''
s = input()
print(s.swapcase())
'''

'''
s = input()
print(s.count(' ') + 1)
'''

'''
s = input()
b = 0
for i in range(10):
    b += s.count(str(i))
print(b)
'''

'''
s = input()
if s.endswith('.ru') or s.endswith('.com'):
    print('YES')
else:
    print('NO')
'''

'''
s = input()
a = s.find('f')
a1 = s.rfind('f')
if a != -1 and a1 != -1 and a1 != a:
    print(a, a1)
elif a != -1 and a1 != -1 and a1 == a:
    print(a)
elif a != -1and a == -1:
    print(a)
else:
    print('NO')
'''

'''
s = input()
a = s.find('h')
a1 = s.rfind('h')
print(s.replace(s[int(a) : int(a1) + 1], ''))
'''

'''
a = ['dfsga', 18888, 1234.456, '342524']   --   это список
b = []      Пустой список
c = list()  Пустой список
чтобы вывести весь список:
print(a)
чтобы вывести элемент списка:
print(a[1])  отсчёт идёт от 0
также функция list может:
a = list(range(5))  преобразовывать все числа от 0 до записынного
b = list(range(0, 10, 2))  преобразовывать все числа из промижутка
c = list('abcd')  преобразовывать строку в список
с списком можно использовать функции:
len;
min;
max;
in;
not in;
sum. если чё sum складывает все числа в списке и выводит полученное значение
также в списке можно заменять определённые части:
a = ['1', '2', '3', '4', '5']
a[2] = '9'
a[-1] = '0'
print(a)
списки можно + * - / :
print([1, 2, 3, 4,] + [5, 6, 7, 8,])
print([7, 8] * 3)
print([0] * 10)
также если в списке есть строка 'fdsgb dfg dzfgdzas!!!' то можно указывать двойной индекс:
a ['2', '34', 'afdgafbgagbfads sghtths gfshsdgh fghstr']
print(a[2][13])
print(a[2][5 : 12])
если в списке указать просто индекс то возмётся элемент списка, НО!!! если взять срез мы создаём новый список:
a = ['dfag', '12', 'agf234']
print(a[1])
print(a[0 : 1])

      МЕТОДЫ СПИСКОВ

a = [1, 1, 2, 3, 5, 8, 13]
a.append(21)  добовляет элемент в конец списка
a.append(34)
print(a)

a = [0, 2, 4, 6, 8, 10]
b = [1, 3, 5, 7]
a.extend(b)  добавлят к списку списек
отличие append('qwert') extend('qwert') в том что 1 добовляет элемент а 2 список состоящий из 1 элемента

a = [1, 1, 2, 3, 5, 8, 13]
del a[5]  удоляет элемент с индексом 5

a = [1, 1, 2, 3, 5, 8, 13]
print(a)
a.insert(0, '223223')
print(a)
a.insert(3, '56457')
print(a)
добовляет элемент в список на выбронное место

a = [1, 1, 2, 3, 5, 8, 13]
b = a.index('3')  находит индекс элемента
print(b)

a = [1, 1, 2, 3, 5, 8, 13]
print(a)
a.remove(3)  удоляет первый элемент значение которого = переданному в скобках
print(a)

a = [1, 1, 2, 3, 5, 8, 13]
print(a)
b = a.pop(2)  удоляет элемент индекс которого = переданному в скобках
print(a)
print(b)

a = [1, 1, 2, 3, 5, 8, 13]
b = a.count(2)
b1 = a.count(1)
b2 = a.count(9)
print(b)
print(b1)
print(b2)

a = [1, 1, 2, 3, 5, 8, 13]
a.reverse()  пишет список задом на перёд
print(a)

a = [1, 1, 2, 3, 5, 8, 13]
a.clear()  удоляет все элементы списка
print(a)

a = [1, 1, 2, 3, 5, 8, 13]
a1 = a.copy()  делает копию списка
print(a1)
'''

'''
a = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]
print(a[16])
print(a[-1])
print(a[0 : 6])
b = [12.5, 3.1415, 2.718, 1.414, 9.8, 1.1618, 1.324]
print(max(b) + min(b))
'''

'''
a = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20,]
b = sum(a) / len(a)
print(b)
'''

'''
a = ['red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'violet']
a[3] = 'Зелённый'
a[6] = 'Фиолетовый'
print(a)
'''

'''
a = []
mar1 = int(input())
mar2 = int(input())
for j in range(8):
    if mar1 == 2 and mar2 != 2:
        f = 1
    else:
        a.append(mar1)
    mar1 = mar2
    mar2 = int(input())
a.append(mar2)
sum0 = 0
b = 0
for i in range(len(a)):
    sum0 += a[b]
    b += 1
sum1 = sum0 / len(a)
sum2 = sum1 * 10
num = int(sum2) % len(a)
if num >= 5:
    ans = int(sum2) // len(a) + 1
else:
    ans = int(sum2) // len(a)
print(ans)
'''

'''
a = []
num = int(input())
for i in range(num):
    str1 = input()
    a.append(str1)
print(a)
'''

'''
num = int(input())
a = []
for i in range(num):
    b = [int(input()), int(input())]
    a.extend(b)
tim = int(input())
ans = 0
ind1 = 0
ind2 = 1
c = 0
for i in range(len(a) - 1):
    while c <= a[ind2]:
        c = a[ind1]
        if c == tim:
            ans += 1
        c += 1
    c = 0
    ind1 += 2
    ind2 += 2
print(ans)
'''