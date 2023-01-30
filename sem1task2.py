# Задача 2
# Найдите сумму цифр трехзначного числа.
# # 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

n = int(input('введите трехзначное число'))
print(n)
n1 = round(n / 100)
n2 = round((n % 100)/10)
n3 = round(n % 10)
print(n1)
print(n2)
print(n3)

res = n1 + n2 + n3
print(res)
