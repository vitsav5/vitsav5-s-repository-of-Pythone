'''
a = 0
b = 0
c = 0
for a in range(24):
    for b in range(60):
        for c in range(60):
            print(a, ':', b, ':', c)
'''

'''
for a in range(3):
    for b in range(3):
        if a == b:
            break
        print(a, b)
'''

'''
for a in range(3):
    for b in range(3):
        if a == b:
            continue
        print(a, b)
'''

'''
for a in range(1, 4):
    for b in range(3, 6):
        print(a, b)
'''

'''
for a in range(1, 4):
    for b in range(3, 5):
        print(a + b, end = '')
'''

'''
a = 0
for i in range(99, 102):
    b = i
    while b > 0:
        a += 1
        b //= 10
print(a)
'''

'''
a = int(input())
if a <= 9:
    for i in range(a):
        print(a, a, a)
else:
    print('а должно быть меньше или = 9')
'''

'''
a = int(input())
if a <= 9:
    for i in range(1, a + 1):
        for i in range(3):
            print(i, i, i, i, i)
else:
    print('а должно быть меньше или = 9')
'''

'''
a = int(input())
for i in range(1, a + 1):
    for j in range(1, 10):
        b = i + j
        print(i, '+', j, '=', b)
    print()
'''

'''
a = int(input())
for i in range(1, a + 1):
    print('')
    for j in range(i):
        print(i, end = '')
'''