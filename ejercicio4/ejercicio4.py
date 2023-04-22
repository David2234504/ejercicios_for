print("-------------------------------------")
print("--------------Factorial--------------")
print("-------------------------------------")

n = int(input("Digite el número al que quiera sacarle el factorial: "))
fact = 1

for i in range(1, n+1):
    fact *= i

print("El factorial de", n, "es", fact)
