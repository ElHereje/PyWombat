'''
d=√((x2-x1)²+(y2-y1)²)
'''
from math import sqrt

print("Datos para el punto X:")
x1 = int(input("Introduce valor x1: "))
x2 = int(input("Introduce valor x2: "))
print()
print("Datos para el punto y:")
y1 = int(input("Introduce valor y1: "))
y2 = int(input("Introduce valor y2: "))

distancia = sqrt((x2-x1)**2 + (y2-y1)**2)
print()
print(f"La distancia entre X e Y es de {distancia} unidades")