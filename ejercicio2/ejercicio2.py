print("-------------------------------------")
print("-----------Múltiplos 7 y 9-----------")
print("-------------------------------------")

num_multiplos_7 = 0
num_multiplos_9 = 0

for i in range(1000, 5001):
    if i % 7 == 0:
        num_multiplos_7 += 1
    if i % 9 == 0:
        num_multiplos_9 += 1

print("Cantidad de múltiplos de 7:", num_multiplos_7)
print("Cantidad de múltiplos de 9:", num_multiplos_9)
