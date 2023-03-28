"""
Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество 
элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
Каждое число вводится с новой строки.
"""
# # Решение
# def fill_array_arith_progress(firstNum, step, arrLen):
#     array = []
#     temp = firstNum
#     for i in range(arrLen):
#         array.append(temp)
#         temp += step
#     return array

# a1 = int(input("Введите первый элемент арифметической прогрессии: "))
# d = int(input("Введите разность арифметической прогрессии: "))
# n = int(input("Введите количество элементов прогрессии: "))
# print(fill_array_arith_progress(a1, d, n))


"""
Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
(т.е. не меньше заданного минимума и не больше заданного максимума)
Ввод:  [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
5
15
Вывод: [1, 9, 13, 14, 19]
"""
# Решение
def fill_array_int_rand(fromNum, toNum, arrLen):  # Создание и рандомное наполнение массива целыми числами 
    import random
    array = []
    for i in range(arrLen):
        array.append(random.randint(fromNum,toNum))
    return array

def find_indexes_in_array(fromNum, toNum, array):
    indexes = []
    for i in range(len(array)):
        if fromNum <= array[i] <= toNum:
            indexes.append(i)
    return indexes


myArray = fill_array_int_rand(-20,20,20)
print()
print("Создан массив из случайных чисел:")
print(myArray)
print()
print("Введите диапазон для поиска в массиве чисел входящих в него:")
num1 = int(input("От: "))
num2 = int(input("До: "))
print("Числа из указанного диапазона находятся на позициях: ")
print(find_indexes_in_array(num1,num2,myArray))
print()

