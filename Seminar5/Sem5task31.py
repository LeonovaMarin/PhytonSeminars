"""Последовательностью Фибоначчи
Требуется найти N-е число Фибоначчи"""


def find_fibo(fibo_lst, x):
    if len(fibo_lst) == x:
        return fibo_lst[-1]
    else:
        fibo_lst.append(fibo_lst[-1] + fibo_lst[-2])
        return find_fibo(fibo_lst, x)
def find_fibo(x, fibo_lst=[0, 1]):  # объявляем ф-цию, где число х - номер числа Фиббоначи, которое надо вывести, + список с первыми двумя числами
    if len(fibo_lst) == x:  # если порядковый номер числа равен длине списка ...
        print(fibo_lst)  # ... печатаем для наглядности список...
        return fibo_lst[-1]   # ... и возвращаем последнее число из списка
    fibo_lst.append(fibo_lst[-1] + fibo_lst[-2])   # добавляем в список новое число
    return find_fibo(x, fibo_lst)   # заходим в рекурсию до тех пор, пока порядковый номер числа не будет равен длине списка


print(find_fibo([0, 1], int(input('Введите номер числа Фиббоначи: '))))
print(find_fibo(int(input('Введите номер числа Фиббоначи: '))))