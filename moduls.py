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