#Задача№4
# 4 - Реализуйте выдачу случайного числа
#  (или алгоритм перемешивания списка)
# не использовать random.randint и вообще 
# библиотеку random
# Можете использовать xor, биты, библиотеку time 
# (миллисекунды или наносекунды) 
# - для задания случайности


import datetime 

min_n = 10
max_n = 100

def get_rand():
    return datetime.datetime.now().microsecond%10

n = get_rand()

print(int(len(str(min_n))))
print(n)