# Pedir dos números enteros al usuario
n = int(input("Ingresa el primer número entero (n): "))
m = int(input("Ingresa el segundo número entero (m): "))


cociente = n // m
resto = n % m

# Mostrar el resultado
print(f"La división de {n} entre {m} da un cociente de {cociente} y un resto de {resto}.")
