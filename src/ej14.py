# Definir el peso de payasos y muñecas en gramos
peso_payaso = 112  # gramos
peso_muneca = 75   # gramos

# Pedir al usuario el número de payasos y muñecas vendidos
num_payasos = int(input("Ingresa el número de payasos vendidos: "))
num_munecas = int(input("Ingresa el número de muñecas vendidas: "))

# Calcular el peso total del paquete
peso_total = num_payasos * peso_payaso + num_munecas * peso_muneca

# Mostrar el resultado
print(f"El peso total del paquete es: {peso_total} gramos.")
