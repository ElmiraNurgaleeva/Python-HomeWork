# #Задача№5 Семинар№6
# Найти произведение пар чисел в списке. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д. 
# #  Пример: [2, 3, 4, 5, 6] => [12, 15, 16]; [2, 3, 5, 6] => [12, 15]

# import random
# import os
# os.system ('cls')

# mas = []
# for i in range(15):
#    mas.append(random.randint(1, 14))
# print('Рандомный список =', mas)

# k = len(mas)
# max = k-1
# proizv = 0
# mas1 = []

# while k >= 2:
   
#    x = int(mas[0])
#    y = int(mas[max])
#    proizv = x * y
#    mas1.append(proizv)
            
#    del mas[max],mas[0]
#    k = k - 2
#    max = k - 1
 
# if k == 1:
#    z = int(mas[0])
#    proizv = z ** 2
#    mas1.append(proizv)
  
#    del mas[0]

# print('Произведения крайних пар массива = ', mas1)


#2й  вариант :

import math

a = [2,3,4,5,6,7,0]
def task23 (a):
    res = []
    for i in range (0,int(math.ceil(len(a)/2))):
        res.append(a[i] * a[len(a)-(i+1)])
    return res
print (task23(a))