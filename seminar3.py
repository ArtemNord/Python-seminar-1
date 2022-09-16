# # Монетки

# n = int(input())
# gerb = 0
# orel = 0
# for i in range(n):
#     k = int(input())
#     if k == 0:
#         gerb += 1
#     else:
#         orel += 1

# print(min(gerb, orel))

# # Монетки

# n = int(input())
# gerb = 0
# orel = 0
# for i in range(n):
#     k = int(input())
#     if k == 0:
#         gerb += 1
#     else:
#         orel += 1

# if gerb < orel:
#     print(gerb)
# else:
#     print(orel)


# # Сумма
# # Требуется посчитать сумму целых чисел, расположенных между числами 1 и N включительно.

# n = int(input())
# print(int(((n + 1) / 2) * n))

# # Минимальный делитель
# # Требуется найти наименьший натуральный делитель целого числа N, отличный от 1.

# n = int(input())
# flag = True
# i = 2
# while flag:
#     if n % i == 0:
#         print(i)
#         flag = False
#     i += 1


# Шеренга
# 8
# 165 163 160 160 157 157 155 154
# 162

# n = int(input())
# arr_rost = list()

# for i in range(n):
#     rost = int(input())
#     arr_rost.append(rost)
    
# # имя_списка.sort()
# # sorted(имя_списка)
# my_rost = int(input())

# j = 1
# for i in arr_rost:
#     if my_rost <= i:
#         j += 1
# print(j)


#Сбор черники

# n = int(input())
# arr = list()
# for i in range(n):
#     # k = int(input())
#     arr.append(int(input()))

# # [1, 2, 3, 4]
# # -4 -3 -2 -1
# maximum = 0
# arr_count = list()
# for i in range(1, len(arr) - 1):
#     arr_count.append(arr[i - 1] + arr[i] + arr[i + 1])
# arr_count.append(arr[0] + arr[1] + arr[-1])
# arr_count.append(arr[-2] + arr[-1] + arr[0])
# print(max(arr_count))


# 1. Реализуйте алгоритм задания случайных чисел без использования встроенного генератора 
# псевдослучайных чисел.

# 2. Задайте список. Напишите программу, которая определит, 
# присутствует ли в заданном списке строк некое число.

# 3. Напишите программу, которая определит позицию второго вхождения
#  строки в списке либо сообщит, что её нет.
# *Пример:*

# - список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# - список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# - список: [], ищем: "123", ответ: -1


# Задача №1

# import time
# from random import randint

# arr = list()
# for i in range(10):
#     number = randint(1, 5)
#     time.sleep(1)
#     arr.append(int(str(time.time())[-number:]))
# print(*arr)

# Задача №2

# arr = ['bbb21dd', 'Hello', 'World']
# n = '21'
# flag = False
# for stroka in arr:
#     if n in stroka:
#         flag = True
#         print('yes')
# if flag == False:
#     print('no')

# Задача №3

