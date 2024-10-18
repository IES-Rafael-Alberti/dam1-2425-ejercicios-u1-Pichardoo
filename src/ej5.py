# Pedir el importe sin IVA y el tipo de IVA
importe_sin_iva = float(input("Ingresa el importe sin IVA del artículo: "))
iva = float(input("Ingresa el porcentaje de IVA a aplicar (por ejemplo, 21 para un 21%): "))


importe_con_iva = importe_sin_iva * (1 + iva / 100)


print(f"El precio final del artículo con IVA es: ${importe_con_iva:.2f}")
