"""Напишите функцию, которая принимает одно число и
проверяет, является ли оно простым"""


def num_is_prime(x):
    count = 0
    for f in range(1, x + 1):
        if x % f == 0:
            count += 1
    if count == 2:
        return True
    else:
        return False
    for f in range(2, x):
        print(f'{f = }')   # строка для визуализации работы рекурсии
        if x % f == 0:   # если число делится на любое число от 2 до х-1, то оно не является простым...
            return 'No'   # выходим из ф-ции
    return 'Yes'   # если прошли по всем числам в цикле и не нашли ни одного делителя х, значит число простое


answer = 'Yes' if num_is_prime(int(input('Введите натуральное число: '))) else 'NO'
print(answer)