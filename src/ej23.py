# Pedir el correo electrónico del usuario
correo = input("Ingresa tu correo electrónico: ")

# Separar el nombre del dominio
nombre, _ = correo.split('@')

# Crear el nuevo correo con el dominio ceu.es
nuevo_correo = f"{nombre}@ceu.es"

# Mostrar el nuevo correo
print(f"Tu nuevo correo electrónico es: {nuevo_correo}")
