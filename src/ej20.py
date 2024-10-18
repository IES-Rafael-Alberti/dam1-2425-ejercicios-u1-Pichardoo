# Pedir el número de teléfono con el formato prefijo-número-extensión
telefono = input("Ingresa el número de teléfono en el formato +34-número-extensión: ")

# Dividir el teléfono para obtener el número sin prefijo y extensión
_, numero, _ = telefono.split('-')


print(f"El número de teléfono es: {numero}")
