# # Округление функция round

# с = 5.65
# print(round(с))

# import math      #импортируем библиотеку math
# a=5.75
# print(math.floor(a))  #Округление в меньшую сторону

# import math
# a=5.75
# print(math.ceil(a))  #Округление в большую сторону

# import math
# print(math.pi)  #Выводим число ПИ


# # # Задача -  Пишем Калькулятор версия2 (v2)

# what = input("Что делаем ? (+,-):")

# a = float(input("Введите первое число :"))
# b = float(input("Введите второе число : "))

# if what == "+":
#     c = a + b
#     print("Результат: " + str(c))

# elif what == "-":
#     c = a - b
#     print("Результат: " + str(c))
# else:
#     print("Выбрана неверная операция ! ")


# x = 3
# y = 4
# z = x + y
# z = z + 1
# x = y
# y = 5
# x = z + y + 7
# print (x)

# Задача СТЕПИК
# Напишите программу вывода на экран трех последовательно
# идущих чисел, каждое на отдельной строке.
# Первое число вводит пользователь, остальные числа вычисляются в программе.
# Формат входных данных
# На вход программе подается одно целое число.
# Формат выходных данных
# Программа должна вывести три последовательно идущих
# числа в соответствии с условием задачи.

# num = int(input("Введите число : "))
# # print(num)
# print("Второе число : ", num + 1)
# print("Третье число : ", num + 2)


# Задача
# Сумма трёх чисел
# Напишите программу, которая считывает три
# целых числа и выводит на экран их сумму.
# Каждое число записано в отдельной строке.

# Формат входных данных
# На вход программе подаётся три целых числа, каждое на отдельной строке.

# Формат выходных данных
# Программа должна вывести сумму введенных чисел.


print(sum([int(input()) for i in range(3)]))

#Задача Степик
