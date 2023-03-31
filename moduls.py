# import moduls      # Импорт всего модуля. Нужно вызывать через имя_модуля.функция
# from moduls import sum_elements    # Импорт только нужной функции
# from moduls import *       # Импорт всех функций из модуля
# import moduls as m1      # Импорт модуля с "псевдонимом" :-)  Вызывается m1.функция

# print(moduls.sum_elements(1,2,3,4,5))
# print(sum_elements(1,2,3,4,5))
# print(m1.sum_elements(1,2,3,4,5))

def sum_elements(*args):  # Сумма нескольких однотипных аргументов
    from typing import Any
    res: Any = args[0]
    for i in args[1:]:
        res += i
    return res

def quick_sort(array):  # Быстрая сортировка
    if len(array) <= 1:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)

def fill_array_rand(fromNum, toNum, arrLen):  # Создание и рандомное наполнение массива целыми числами 
    import random
    array = []
    for i in range(arrLen):
        array.append(random.randint(fromNum,toNum))
    return array

def merge_sort(array):  # Сортировка слиянием
    if len(array) > 1:
        mid = len(array) // 2
        left = array[:mid]
        right = array[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1