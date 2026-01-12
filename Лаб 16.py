'''
a = input()
n = 0
m = 0
for c in a:
    if c in '*':
        m += 1
    if c in '+':
        n += 1
print('Символ + встречается', n, 'раз')
print('Символ * встречается', m, 'раз')
'''

'''
Срезы
s = 'abcdefghij'
print(s[2:5])
print(s[0:6])
print(s[2:7])
print(s[2:])
print(s[:7])
print(s[:])
print(s[-9:-4])
print(s[-3:0])
print(s[:-3])
Шаг в срезе
print(s[1:7:2])
print(s[::-1])
print(s[::-2])
'''

'''
s = input()
a = s[:]
b = s[::-1]
if a == b:
    print('YES')
else:
    print('NO')
'''

'''
s = input()
a = len(s)
print(a)
print(s, s, s)
print(s[:1])
print(s[:3])
print(s[-3:])
print(s[::-1])
print(s[1:a - 1])
'''

'''
s = 'a1b2c3d4e5f6g7h8i9'
for i in range(0, len(s), 2):
    print(s[i], end = '*')
'''

#    Методы
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
'''

#     Методы поиска и замены
'''
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
print(s.kfind('ds\dsf')) #  Ищет первое сочетание знаков с конца и выдаёт индекс где они начинаются (если такого нет то выводит -1)
print(s.strip())
print(s.lstrip())
print(s.rstrip())
print(s.replace('foo', 'sdfagfa')) # Замена чего то на что то
'''
