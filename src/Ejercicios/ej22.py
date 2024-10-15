# Pedir al usuario que introduzca una frase
frase = input("Ingresa una frase: ")

# Pedir una vocal
vocal = input("Ingresa una vocal: ")

# Reemplazar la vocal en la frase por su versión en mayúscula
frase_modificada = frase.replace(vocal, vocal.upper())

# Mostrar la frase modificada
print(f"La frase modificada es: {frase_modificada}")
