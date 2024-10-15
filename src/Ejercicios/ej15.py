# Leer la cantidad de dinero depositada
capital_inicial = float(input("Ingresa la cantidad de dinero depositada en la cuenta: "))

# Definir el interés anual
interes_anual = 0.04

# Calcular el balance después del primer, segundo y tercer año
capital_ano1 = capital_inicial * (1 + interes_anual)
capital_ano2 = capital_ano1 * (1 + interes_anual)
capital_ano3 = capital_ano2 * (1 + interes_anual)

# Mostrar los resultados redondeados a dos decimales
print(f"El balance tras el primer año es: ${capital_ano1:.2f}")
print(f"El balance tras el segundo año es: ${capital_ano2:.2f}")
print(f"El balance tras el tercer año es: ${capital_ano3:.2f}")

