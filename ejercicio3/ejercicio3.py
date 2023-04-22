print("-------------------------------------")
print("------------Cara de dados------------")
print("-------------------------------------")

import random

n = int(input("Ingrese la cantidad de lanzamientos de dados: "))
cara1 = 0
cara2 = 0
cara3 = 0
cara4 = 0
cara5 = 0
cara6 = 0

for i in range(n):
    cara = random.randint(1, 6)
    if cara == 1:
        cara1 += 1
    if cara == 2:
        cara2 += 1
    if cara == 3:
        cara3 += 1
    if cara == 4:
        cara4 += 1
    if cara == 5:
        cara5 += 1
    if cara == 6:
        cara6 += 1
     
print("Frecuencias:")
print("1:"+"*" * cara1)
print("2:"+"*" * cara2)
print("3:"+"*" * cara3)
print("4:"+"*" * cara4)
print("5:"+"*" * cara5)
print("6:"+"*" * cara6)


