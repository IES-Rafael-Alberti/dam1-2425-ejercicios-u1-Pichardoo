import math

def calcular_area_triangulo(a, b, c):
    # Calcular el semiperímetro
    s = (a + b + c) / 2
    
    # Calcular el área usando la fórmula de Herón
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    
    return area


def main():
    # Ejemplo de uso
    a = 3
    b = 4
    c = 5
    area = calcular_area_triangulo(a, b, c)
    print(f"El área del triángulo con lados {a}, {b} y {c} es: {area:.2f}")



main()