# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.

from random import randint
coins_num = int(input('введите количество монеток'))
coin_eagles, coin_tails = 0, 0
for _ in range(coins_num):
    temp = randint(0, 1)
    print(temp, end=' ')
    if temp == 0:
        coin_eagles += 1
    else:
        coin_tails += 1
if coin_tails > coin_eagles:
    print(f'количество монет, которое нужно перевернуть {coin_eagles}')
else:
    print(f'количество монет, которое нужно перевернуть {coin_tails}')