# Задача №39. Решение в группах
# Даны два массива чисел. Требуется вывести те элементы
# первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. Пользователь вводит
# число N - количество элементов в первом массиве, затем N
# чисел - элементы массива. Затем число M - количество
# элементов во втором массиве. Затем элементы второго массива
# Ввод: Вывод:
# 7 3 3 2 12
# 3 1 3 4 2 4 12
# 6
# 4 15 43 1 15 1 (каждое число вводится с новой строки)

def numbers(x):
    list_1 = []
    for _ in range(x):
        list_1.append(int(input('Введите элемент массива')))
    return list_1

def diff_list(list_1, list_2):
    list_3 = []
    for i in list_1:
        if i not in list_2:
            list_3.append(i)
        return list_3

n = int(input('Введите количество элементов первого массива'))
list_n = numbers(n)
print(list_n)
m = int(input('Введите количество элементов второго массива'))
list_m = numbers(m)
print(list_m)

print(diff_list(list_m, list_n))

# def lst_diff2(list_1: list, list_2: list):
# return [i for i in list_1 if i not in list_2]

