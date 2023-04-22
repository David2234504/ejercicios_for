print("-------------------------------------")
print("-----------Pares e impares-----------")
print("-------------------------------------")

num_pares = 0
num_impares = 0

n = int(input("Ingrese la cantidad de números a leer: "))
for i in range(n):
    num = int(input("Ingrese un número entero: "))
    if num % 2 == 0:
        num_pares += 1
    else:
        num_impares += 1

print("Cantidad de números pares:", num_pares)
print("Cantidad de números impares:", num_impares)
