#Задача№1
#  - Напишите программу, которая принимает на вход 
#  вещественное число и показывает сумму его цифр.

# *Пример:*

# - 6782 -> 23
# - 0,56 -> 11


number  = input ('Введите вещественное число : ')
result = 0
for i in range (len(number)):
    if number[i].isdigit():
        result += int (number [i])
print('Сумма равна : ', result)
