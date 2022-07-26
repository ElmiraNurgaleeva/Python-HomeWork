#Задача№6 Семинар№6
# Сформировать список из  N членов последовательности.
# Для N = 5: 1, -3, 9, -27, 81 и т.д.

# print()
# print('Задача 1 => Сформировать список из  N членов последовательности. ')
# print('Для N = 5: 1, -3, 9, -27, 81 и т.д.')
# print()
# N = int(input('Введите число: '))

# list = []

# for i in range(N):
#     list.append((-3)**i)
# print(list)

# print()


#2й вариант 


my_list = [1, 3, 6, 3, 6, 12]
new_list = []

# def f_1(x):
#     global new_list
#     if x not in new_list:
#         new_list.append(x)

# f = lambda x: new_list.append(x) if x not in new_list else False

res = list(filter(lambda x: new_list.append(x) if x not in new_list else False, my_list))
print(new_list)