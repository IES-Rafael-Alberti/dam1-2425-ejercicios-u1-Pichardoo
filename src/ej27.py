# Pedir el nombre del producto, su precio y el número de unidades
nombre_producto = input("Ingresa el nombre del producto: ")
precio = float(input("Ingresa el precio del producto: "))
unidades = int(input("Ingresa el número de unidades: "))

# Calcular el coste total
coste_total = precio * unidades


print(f"{nombre_producto} {precio:6.2f}€ {unidades:3d} unidades {coste_total:8.2f}€")
