# Pedir la fecha de nacimiento
fecha = input("Ingresa tu fecha de nacimiento (dd/mm/aaaa): ")

# Reemplazar el delimitador '/' con un espacio para separar los valores
fecha_separada = fecha.replace('/', ' ').split()

# Extraer el día, mes y año
dia = fecha_separada[0].zfill(2)  
mes = fecha_separada[1].zfill(2) 
año = fecha_separada[2]


print(f"Día: {dia}")
print(f"Mes: {mes}")
print(f"Año: {año}")
