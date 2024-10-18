# Pedir el precio de un producto
precio = input("Ingresa el precio del producto en euros (con dos decimales): ")

# Separar euros y céntimos
euros, centimos = precio.split('.')


print(f"Euros: {euros}€")
print(f"Céntimos: {centimos} céntimos")
