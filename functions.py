# два числа A и B, и возводит число А в целую степень B с помощью рекурсии

def NumberDegree(n, d):
    if d == 0:
        return 1 
    return n * (NumberDegree(n, d - 1))

# рекурсивная функция sum(a, b), двух целых неотрицательных чисел
#  до 996+996 считает, если n1 и 1 поменять местами считает до 997+997
def NumberSum(n1, n2):
    if n2 < 0:
        return 0 
    return n1 + (NumberSum(1, n2 - 1))

# найти N-е число Фибоначчи
def last_fibon(n):
    if n in [0, 1]:
        return n
    return last_fibon(n-1) + last_fibon(n-2)

#функция создания массива с поочерёдным вводом элементов
def input_array(size):
    array = []
    for i in range(size) :
        input_element1 = int(input(f'{i + 1} элемент массива: '))
        array.append(input_element1)
    return array

# функция принимает два массива и выводит те элементы первого массива 
# (в том порядке, в каком они идут в первом массиве), которых нет во втором массиве
def absence_elements(arr_1, arr_2):
    result_arr = []
    for i in arr_1:
        if i not in arr_2:
            result_arr.append(i)
    return result_arr

#считает сколько пар элементов в списке, равных друг другу
def counting_couples(arr):    
    count=0
    arr2=[]
    for i in range(len(arr)):
        if arr[i] in arr2:
            count+=1
            arr2.remove(arr[i])
        else:
            arr2.append(arr[i])
    return count

#считает сколько пар элементов в списке, равных друг другу
def pairs_count(array):
    count = 0
    for n in set(array):
        count += array.count(n) // 2
    return count

# находит сумму дружественныx числeл
def sum_of_dividers(num):
    sum = 1
    for i in range(2, num // 2 + 1):
        if num % i == 0 :
            sum += i
    return sum

#данному числу k выводит все пары дружественных чисел, каждое из которых не превосходит k
def frendly_numbers(k):
    for i in range(2, k):
        partner = sum_of_dividers(i)
        if i == sum_of_dividers(partner) and i > partner:
            print(f'{i} - {partner}')

# заменяет элементы списка максимальные на минимальные.
def replace_min_max(array):
    for i in range(len(array)):
        if array[i] == max(array):
            array[i] = min(array)
    return array

# проверяет, является ли число простым
def is_simple(number):
    if number > 2 and  number % 2 !=0 :
        for i in range (3, number // 2):
            if number % i == 0:
                return False
        return True
    return False

# выводит в обратном порядке числа от 0 до n
def reverse_range(num):
    print(num, end = ' ')
    if num > 0: 
        reverse_range(num - 1)
    print(num, end = ' ')
