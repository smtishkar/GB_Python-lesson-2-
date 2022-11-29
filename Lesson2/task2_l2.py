# 2'. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# *Пример:*
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

import math
# number = int(input('Введите любое положительное число: '))
# list = []
# n = 1
# count = 1

# for i in range (number):
#     list.append(n)
#     count += 1
#     n = n * count
# print(list)



#Второй вариант

n = int(input('Введите любое положительное число: '))
mult = [math.factorial (i) for i in range(1, n+1)]  # Генерация списка (до for что добавляем, после for по какому принципу)
print (f"result {mult}")