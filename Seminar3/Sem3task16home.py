#  Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai
# . Последняя строка содержит число X

n = int(input('введите натуральное число N – количество элементов в массиве'))
x = int(input('число X, которое встречается в массиве A'))
from random import randint
a = [randint(1, 10) for i in range(n)]
print(a)
count = 0
for i in a:
    if i == x:
        i += 1
        count += 1
        print(f'число x={x} встречается в заданном массиве {count} раз')
    else:
        print('заданное число в массиве отсутствует')
        break
