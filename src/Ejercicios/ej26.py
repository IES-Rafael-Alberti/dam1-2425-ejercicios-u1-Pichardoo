# Pedir los productos de la cesta de la compra
productos = input("Ingresa los productos de la cesta de la compra, separados por comas: ")

# Separar los productos usando la coma como delimitador y eliminar espacios
lista_productos = [producto.strip() for producto in productos.split(',')]

# Mostrar cada producto en una línea distinta
for producto in lista_productos:
    print(producto)
