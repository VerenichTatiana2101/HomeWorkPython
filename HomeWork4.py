# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, 
# которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. 
# m — кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.

#в данной задаче использую списки, а не функцию сплит для ввода
#лишь по той причине, что нужно ограничить пользователя в количестве
#вводимых элементов, split позволяет обрезать количество элементов, но это не подходит

"""
size1 = int(input('Введите количество элементов первого набора: '))
size2 = int(input('Введите количество элементов второго набора: '))

array1 = []
for i in range(size1) :
    input_element1 = input(f'{i + 1} элемент первого набора: ')
    array1.append(input_element1)
result1 = set(array1)

array2 = []
for i in range(size2) :
    input_element2 = input(f'{i + 1} элемент второго набора: ')
    array2.append(input_element2)
result2 = set(array2)

answer = result1.intersection(result2)
print(*array1)
print(*array2)
print(sorted(answer))
"""

#с проверкой вводимых данных
# size1 = input('Введите количество элементов первого набора: ')
# size2 = input('Введите количество элементов второго набора: ')

# if size1.isdigit() and size2.isdigit() : 
#     size1 = int(size1)
#     size2 = int(size2)
#     if size1 > 0 and size2 > 0 :
#         array1 = []
#         for i in range(size1) :
#             input_element1 = input(f'{i+1} элемент первого набора: ')
#             array1.append(input_element1)
#         result1 = set(array1)

#         array2 = []
#         for i in range(size2) :
#             input_element2 = input(f'{i+1} элемент второго набора: ')
#             array2.append(input_element2)
#         result2 = set(array2)

#         answer = result1.intersection(result2)
#         print(*array1)
#         print(*array2)
#         print(sorted(answer))
#     else:
#         ('Данные введены некорректно')
# else:
#     print('Данные введены некорректно')


# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. 
# Она растёт на круглой грядке, причём кусты высажены только по окружности. 
# Таким образом, у каждого куста есть ровно два соседних. 
# Всего на грядке растёт N кустов.
# Эти кусты обладают разной урожайностью, 
# поэтому ко времени сбора на них выросло различное число ягод — на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. 
# Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, 
# собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, 
# которое может собрать за один заход собирающий модуль, 
# находясь перед некоторым кустом заданной во входном файле грядки.

"""
numinput_element2er_input_element2ushes = int(input('Введите количество кустов на грядке: '))
numinput_element2er_input_element2erries = []
for i in range(numinput_element2er_input_element2ushes) :
    numinput_element2er_input_element2erries.append(int(input(f'Количество ягод на {i + 1} кусте: ')))
print(numinput_element2er_input_element2erries)    

sum_input_element2erries = []
for i in range(len(numinput_element2er_input_element2erries) - 1) :
    sum_input_element2erries.append(numinput_element2er_input_element2erries[i] 
                       + numinput_element2er_input_element2erries[i - 1] 
                       + numinput_element2er_input_element2erries[i + 1])
sum_input_element2erries.append(numinput_element2er_input_element2erries[-2] + numinput_element2er_input_element2erries[-1] + numinput_element2er_input_element2erries[0])
print(max(sum_input_element2erries))
"""