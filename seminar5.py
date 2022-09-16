# Суперсдвиг
# n = int(input())
# list_first = list()
# list_result = [0] * n
# for i in range(n):
#     list_first.append(int(input()))
# print(*list_first)

# k = int(input())
# k = k % n
# if k > 0:
#     for i in range(k):
#         list_result[i] = list_first[n - k + i]
#     for i in range(n - k):
#         list_result[k + i] = list_first[i]
#     print(*list_result)
# else:
#     k = -k
#     for i in range(k):
#         list_result[i] = list_first[n - k + i]
#     for i in range(n - k):
#         list_result[k + i] = list_first[i]
#     print(*list_result)

# НегаФибоначчи

# list_1 = list()
# a0 = 0
# a1 = 1
# n = int(input())
# for i in range(n + 1):
#     list_1.append(a0)
#     x = a0 + a1
#     a0 = a1
#     a1 = x
# list_2 = [list_1[i] * (-1) ** (i + 1) for i in range(len(list_1))][::-1]
# print(list_2 + list_1[1:])

# ---------------------------------------------

# a, b = map(lambda x: int(x), input().split())
# print(a + b)

# arr = [int(i) for i in input().split()]
# print(arr)

# 35. В файле находится N натуральных чисел, записанных через пробел. 
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i - 1]. 
# Найдите это число.

# 36. Дан список чисел. Создайте список, в который попадают числа, 
# описываемые возрастающую последовательность. 
# Порядок элементов менять нельзя.
#     *Пример:* 
#     [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.

# 37. Напишите программу, удаляющую из текста все слова, содержащие "абв".


# 35

# def search_number(arr):
#     for i in range(1, len(arr)):
#         if arr[i] - 1 != arr[i - 1]:
#             return i + 1
#     return 'Последовательность верна'


# with open('1.txt', 'r', encoding='utf-8') as file:
#     arr = [int(i) for i in file.read().split()]
# print(search_number(arr))


# 36

arr = [1, 5, 2, 3, 4, 6, 1, 7]
arr_result = []
for i in range(len(arr)):
    arr_result = arr[i]
    if arr[i] > arr_result[i - 1]:
        arr_result.append(arr[i])