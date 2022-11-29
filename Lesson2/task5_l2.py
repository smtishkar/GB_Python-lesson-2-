# 5'. Реализуйте алгоритм перемешивания списка.

# Сделал 3мя разными методами, т.к. не очень понятно было как делать правильно. Мне больше всего 
# понравился 2ой вариант, наверное, он наиболее правильный.



from random import randint 
from random import shuffle


# Перемешивание при помощи метода

# n = int(input('введите длину списка: '))
# list =[]

# for i in range(n):
#     list.append(randint(-10,10))

# print(f'Список до перемешивания    {list}')
# shuffle(list)
# print(f'Список после перемешивания {list}')






# Перемешивание случайных элементов

n = int(input('введите длину списка: '))
list =[]

for i in range(n):
    list.append(randint(-10,10))

print(f'Список до перемешивания    {list}')

for i in range(len(list)-1):
    j = randint(0, len(list)-2)
    temp = list[i]
    list[i] = list [j]
    list [j] = temp
print(f'Список после перемешивания {list}')



# Перемешивание соседних элементов 

# n = int(input('введите длину списка: '))
# list =[]

# for i in range(n):
#     list.append(randint(-10,10))

# print(f'Список до перемешивания    {list}')

# for i in range(len(list)-1):
#     temp = list[i]
#     list[i] = list [i+1]
#     list [i+1] = temp
# print(f'Список после перемешивания {list}')



