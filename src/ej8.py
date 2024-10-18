# Usar solo dos variables para los tres números
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

# Sobreescribir una variable para almacenar el tercer número y calcular la suma
num1 = num1 + float(input("Ingresa el tercer número: "))

# Sumar los dos valores y mostrar el resultado
suma = num1 + num2
print(f"La suma de los tres números es: {suma}")
