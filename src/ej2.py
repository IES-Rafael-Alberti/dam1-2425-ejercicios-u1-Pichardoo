# Pedir las horas de trabajo y el precio por hora
horas_trabajadas = float(input("Ingresa las horas trabajadas: "))
precio_por_hora = float(input("Ingresa el precio por hora: "))

# Calcular el importe total
importe_total = horas_trabajadas * precio_por_hora

# Mostrar el resultado
print(f"El importe total por el servicio es: ${importe_total:.2f}")
