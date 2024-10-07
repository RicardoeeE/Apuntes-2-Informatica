def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

def superfactorial(n):
    if n <= 0 or n >= 10:
        return "El número debe ser mayor que 0 y menor que 10"
    
    superfact = 1
    for i in range(1, n + 1):
        superfact *= factorial(i)
    return superfact

# Ejemplo
n = int(input("Introduce un número mayor que 0 y menor que 10: "))
print("El superfactorial de", n, "es:", superfactorial(n))
