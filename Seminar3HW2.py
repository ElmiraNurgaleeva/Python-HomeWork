#Задача№2
# 2 - Напишите программу, которая найдёт 
# произведение пар чисел списка. Парой считаем 
# первый и последний элемент, второй и предпоследний и т.д.

# *Пример:*

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

def product_pairs_numbers(list):
    product = []
    for i in range((len(list)+1)//2):
        product.append(list[i]*list[len(list)-1-i])
    return product

init_list = [2, 3, 4, 5, 6]
print(init_list, end=' => ')
print(product_pairs_numbers(init_list))
