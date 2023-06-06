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