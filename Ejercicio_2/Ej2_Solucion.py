def mostrar_escalera():
    while True:
        try:
            escalones = int(input("Introduce el número de escalones (>0): "))
            if escalones < 1:
                print("Error en el rango. Introduce el número (>0):")
                continue
            break
        except ValueError:
            print("Por favor, introduce un número entero.")

    for i in range(1, escalones + 1):
        for j in range(1, i + 1):
            print(j, end=' ')
        print()  # Salto de línea después de cada escalón

# Llamamos a la función
mostrar_escalera()
