# Pedir el importe final del artículo
importe_final = float(input("Ingresa el importe final del artículo (con IVA): "))

# Suponiendo un IVA del 10%
tipo_iva = 10


importe_sin_iva = importe_final / (1 + tipo_iva / 100)


iva_pagado = importe_final - importe_sin_iva


print(f"El importe sin IVA es: ${importe_sin_iva:.2f}")
print(f"El IVA pagado es: ${iva_pagado:.2f}")   