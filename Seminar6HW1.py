#Задача№1 Семинар№6
# Определить, присутствует ли в заданном списке строк, некоторое число

# str_list = ['Определить, присутствует ли', 'в заданном списке строк,', 'некоторое число (3)']
# present_flag = False
# n = 3

# for i in str_list:
#     for j in i:
#         if j == 'n':
#             present_flag = True
# if present_flag:
#     print('Есть!')
# else:
#     print('Нет')


#2й вариант

import numbers


list = ['asd', 'a5k', '6', '50']

def find (arr, n):
    string = ''.join(arr)
    return str(n) in string
   
print(find(list, 6))