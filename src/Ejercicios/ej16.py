# Precio habitual de una barra de pan
precio_barra = 3.49

# Descuento del 60% por barras no frescas
descuento = 0.60

# Pedir al usuario el número de barras no frescas vendidas
num_barras = int(input("Ingresa el número de barras no frescas vendidas: "))

# Calcular el precio total con descuento
precio_descuento = precio_barra * (1 - descuento)
coste_total = num_barras * precio_descuento

# Mostrar los resultados
print(f"El precio habitual de una barra de pan es: {precio_barra:.2f}€")
print(f"El descuento por no ser fresca es: {descuento * 100}%")
print(f"El coste total por las barras no frescas es: {coste_total:.2f}€")
