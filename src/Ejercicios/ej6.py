# Pedir el importe final del artículo
importe_final = float(input("Ingresa el importe final del artículo (con IVA): "))

# Suponiendo un IVA del 10%
tipo_iva = 10

# Calcular el importe sin IVA
importe_sin_iva = importe_final / (1 + tipo_iva / 100)

# Calcular el IVA pagado
iva_pagado = importe_final - importe_sin_iva

# Mostrar los resultados
print(f"El importe sin IVA es: ${importe_sin_iva:.2f}")
print(f"El IVA pagado es: ${iva_pagado:.2f}")   