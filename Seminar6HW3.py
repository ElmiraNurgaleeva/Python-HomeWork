#Задача№3 Семинар№6
# Найти расстояние между двумя точками пространства
# (числа вводятся через пробел)

# x1,y1=map(int,input('Введите координаты X и Y для первой точки: ').split())
# x2,y2=map(int,input('Введите координаты X и Y для второй точки: ').split())
# interval=(((x2-x1)**2)+((y2-y1)**2))**0.5
# print('Расстояние между точками в пространстве = ', interval)

#2й  вариант :

firstPoint= list(map(int, input("Введите координаты первой точки x y z через пробел (например:  2 3 4):").split()))
secondPoint= list(map(int, input("Введите координаты второй точки x y z через пробел (например:  2 3 4):").split()))
result = (((secondPoint[0] - firstPoint[0])**2) + ((secondPoint[1] - firstPoint[1])**2) + ((secondPoint[2] - firstPoint[2])**2))**(1/2)
print(f"Расстояние между двумя точками пространства = {round(result, 2)}")