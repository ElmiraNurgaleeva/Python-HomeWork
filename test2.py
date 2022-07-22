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


#Задача Определение погоды

import pyowm

owm = OWM('976410ea676f8e3aa379626cba3e1f85')
observation = mgr.weather_at_place('London,GB')
w = observation.weather
print(w)

