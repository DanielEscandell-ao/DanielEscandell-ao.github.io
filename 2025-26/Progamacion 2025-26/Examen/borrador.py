n = int(input("Introdueix un nombre sencer: "))

suma = 0
i = 1

while i <= n // 2:
    if n % i == 0:
        suma = suma + i
    i = i + 1

print("La suma dels divisors és:", suma)
