# 1. Задайте строку из набора чисел. Напишите программу, которая покажет большее и 
#    меньшее число. В качестве символа-разделителя используйте пробел.

# 2. Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:
    
#     1) с помощью математических формул нахождения корней квадратного уравнения
    
#     2) с помощью дополнительных библиотек Python
    
# 3. Задайте два числа. Напишите программу, которая 
#    найдёт НОК (наименьшее общее кратное) этих двух чисел.

# D = b ** 2 - 4 * a * c
# x1 = (-b + sqrt(D)) // 2 * a
# x2 = (-b - sqrt(D)) // 2 * a


# (Алгорит Евклида) - НОД
# НОК = (a * b) / НОД(a, b)

# 1.

# string = '123 32 4 -59 87 65'
# intstring = string.split(' ')

# for i in range(len(intstring)):
#     intstring[i] = int(intstring[i])

# minnum = 0
# maxnum = 0

# for i in range(len(intstring)):
#     if intstring[i] > minnum:
#         maxnum = intstring[i]
#     else:
#         minnum = intstring[i]

# print(minnum, maxnum)

# 2. Ax² + Bx + C = 0

# from math import sqrt


# A = int(input('Число А: '))
# B = int(input('Число B: '))
# C = int(input('Число C: '))
# D = B * B - 4 * A * C
# if D > 0:
#     x1 = ((-B) + D ** 0.5) / 2 * A
#     x2 = ((-B) - sqrt(D)) / 2 * A
#     print(round(x1, 3), round(x2, 3))
# elif D == 0:
#     x1 = (-B) / 2 * A
#     print(x1)
# else:
#     print('корней нет')

# 3. 

from random import randrange


numA = int(randrange(1, 100))
numB = int(randrange(1, 100))
p = numA * numB

while numA != 0 and numB != 0:
    if numA > numB:
        numA = numA % numB

