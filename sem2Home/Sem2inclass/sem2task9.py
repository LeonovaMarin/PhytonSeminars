# Задача №9. Решение в группах
# По данному целому неотрицательному n вычислите
# значение n!. N! = 1 * 2 * 3 * … * N (произведение всех
# чисел от 1 до N) 0! = 1 Решить задачу используя цикл
# while
# Input: 5
# Output: 120

# n = int(input())
# i = 1
# k = 1
# for i in range(n+1):
#     N = N * i
# print(N)

def factorial(k):
    counter = 1
    res = 1
    while counter <= k:
        res *= counter
        counter += 1
    return res


a = int(input('введите число: '))
print(f'факториал числа{a} {factorial(a)}')



