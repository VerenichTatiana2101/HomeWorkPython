# Задача 10:
# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть

while True:
    n = input('Введите количество монет: ')
    if n.isdigit():
        n = int(n)
        i = 0
        count_one = 0
        count_null = 0
        import random
        random_array = [random.randint(0, 1) for i in range(n)]
        print(random_array)
        for i in range(n):
            if random_array[i] == 1:
                count_one += 1
            else: count_null += 1
        if count_one > count_null:
            print('Минимальное количество монет, которые нужно перевернуть -' ,count_null)
        else:
            print('Минимальное количество монет, которые нужно перевернуть -', count_one)