from random import randint
n = int(input('Введите количество элементов '))
a = [randint(0,1) for i in range(n)]
print(a)
for i in range(1,n+1):
    h, c0, c1 = 0, 0, 0
    for k in range(n):
        if len(a[k:k+i]) == i:
            h += 1
            s = a[k:k+i]
            if sum(s) == 0: c0 += 1
            if sum(s) == i: c1 += 1
    if c0 != 0 and c1 != 0:
        print('Вероятность ', '0' * i, f'- {c0 / h}')
        print('Вероятность ', '1' * i, f'- {c1 / h}')