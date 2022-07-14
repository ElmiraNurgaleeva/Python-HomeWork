#Задача№3
# 3 - Задайте список из вещественных чисел.
#  Напишите программу, которая найдёт разницу 
#  между максимальным и минимальным значением 
#  дробной части элементов.

# *Пример:*

# - [1.1, 1.2, 3.1, 5.561, 10.01] => 0.56 или 56

def difference_max_min(lst):
    result = []
    for index in range(len(lst)):
        result.append(round(lst[index]%1, 2))

    return max(result) - min(result)

my_list = [1.1, 1.2, 3.1, 5.561, 10.01]
print(f'{my_list} => {difference_max_min(my_list)}')