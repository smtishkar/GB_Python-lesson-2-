# 1'. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# *Пример:*
# - 6782 -> 23
# - 0,56 -> 11


number = (input('Введите любое положительное число: '))
number = number.replace(',','')
number = int(number)
sum = 0

while number > 0:
    sum = sum + (number % 10)
    number = number // 10
    print (sum, number)

print(sum)