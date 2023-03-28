# МОДУЛИ

# import moduls      # Импорт всего модуля. Нужно вызывать через имя_модуля.функция
# from moduls import sum_elements    # Импорт только нужной функции
# from moduls import *       # Импорт всех функций из модуля
# import moduls as m1      # Импорт модуля с "псевдонимом" :-)  Вызывается m1.функция

# print(moduls.sum_elements(1,2,3,4,5))
# print(sum_elements(1,2,3,4,5))
# print(m1.sum_elements(1,2,3,4,5))

# РЕКУРСИЯ

# def fib(n):
#     if n in [1,2]:
#         return 1
#     return fib(n-1) + fib(n-2)

# list1 = []
# for i in range(1,10):
#     list1.append(fib(i))
# print(list1)

# Быстрая сортировка

def quick_sort(array):
    if len(array) <= 1:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)
    
print(quick_sort([5,8,9,6,4,7,3,2,6,11,25,69,98]))