#Задача№1 Семинар4

# Вычислить число ПИ c заданной точностью d

# Пример:

# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

import math
from decimal import Decimal
d = input("Введите число d = ")
p = Decimal((math.pi)).quantize(Decimal(d))
print("ПИ = :", p)