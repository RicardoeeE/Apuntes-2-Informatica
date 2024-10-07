# Apuntes de Sentencias de Control Básicas en Python

## 1. Sentencia `if`

La sentencia `if` se utiliza para ejecutar un bloque de código solo si se cumple una condición.

### Sintaxis:
```python
if condición:
    # código a ejecutar si la condición es verdadera
elif otra_condición:
    # código a ejecutar si la primera condición es falsa y la otra_condición es verdadera
else:
    # código a ejecutar si ninguna de las condiciones anteriores es verdadera
```

### Ejemplo:
```python
x = 10
if x > 0:
    print("x es positivo")
elif x == 0:
    print("x es cero")
else:
    print("x es negativo")
```

### Casos de uso:
- Validar entradas de usuario.
- Tomar decisiones basadas en valores.
- Manejar condiciones múltiples.

---

## 2. Sentencia `while`

El bucle `while` permite ejecutar repetidamente un bloque de código mientras una condición sea verdadera.

### Sintaxis:
```python
while condición:
    # código a ejecutar mientras la condición sea verdadera
```

### Ejemplo:
```python
i = 1
while i <= 5:
    print(i)
    i += 1
```

### Uso del `break`:
El `break` permite salir de un bucle antes de que la condición se vuelva falsa.
```python
i = 1
while True:
    print(i)
    i += 1
    if i > 5:
        break
```

### Casos de uso:
- Ejecutar tareas repetitivas.
- Búsqueda de elementos o condiciones.
- Simulaciones.

---

## 3. Sentencia `for`

El bucle `for` en Python se utiliza para iterar sobre una secuencia (lista, tupla, diccionario, conjunto o cadena).

### Sintaxis:
```python
for variable in secuencia:
    # código a ejecutar para cada elemento de la secuencia
```

### Ejemplo:
```python
for letra in "Python":
    print(letra)
```

### Uso del `break`:
El `break` interrumpe el bucle cuando se cumple una condición.
```python
for i in range(10):
    if i == 5:
        break
    print(i)
```

### Casos de uso:
- Iterar sobre colecciones (listas, cadenas, etc.).
- Manipulación de datos en estructuras iterables.
- Recorrer rangos de valores.

---

## 4. Función `range`

La función `range()` genera una secuencia de números, útil para controlar bucles `for` en Python.

### Sintaxis:
```python
range(start, stop, step)
```
- `start`: valor inicial (opcional, por defecto es 0).
- `stop`: valor final (no incluido).
- `step`: incremento (opcional, por defecto es 1).

### Ejemplos:

#### Caso básico:
```python
for i in range(5):  # Genera números desde 0 hasta 4 (5 no está incluido)
    print(i)
```

#### Con parámetros:
```python
for i in range(2, 10, 2):  # Genera números del 2 al 8 en saltos de 2
    print(i)
```

### Verificar si un número está en el rango:
```python
print(3 in range(1, 5))  # True porque 3 está en el rango 1-4
print(5 in range(1, 5))  # False porque 5 no está en el rango 1-4
```

### Casos de uso:
- Control de bucles en rangos numéricos.
- Generar secuencias para manipular listas.
- Crear bucles con saltos específicos.

---

## 5. Bucles Anidados

Es posible anidar un bucle dentro de otro para manejar estructuras más complejas.

### Sintaxis:
```python
for variable1 in secuencia1:
    for variable2 in secuencia2:
        # código a ejecutar en cada iteración anidada
```

### Ejemplo de bucles `for` anidados:
```python
for i in range(3):
    for j in range(2):
        print(f"i: {i}, j: {j}")
```
Salida:
```
i: 0, j: 0
i: 0, j: 1
i: 1, j: 0
i: 1, j: 1
i: 2, j: 0
i: 2, j: 1
```

### Uso del `break` en bucles anidados:
El `break` solo interrumpe el bucle en el que está ubicado.
```python
for i in range(3):
    for j in range(2):
        if j == 1:
            break
        print(f"i: {i}, j: {j}")
```

### Ejemplo con `while` y `for`:
```python
i = 0
while i < 3:
    for j in range(2):
        print(f"i: {i}, j: {j}")
    i += 1
```

### Casos de uso:
- Trabajar con estructuras de datos en varias dimensiones (matrices, listas anidadas).
- Procesar varias colecciones en paralelo.
- Resolver problemas que requieren múltiples iteraciones anidadas.

---

## 6. Casos de Uso Comunes de `range` y Bucles Anidados

### Generar una matriz:
```python
matriz = []
for i in range(3):
    fila = []
    for j in range(3):
        fila.append(i * j)
    matriz.append(fila)
print(matriz)
```
Salida: `[[0, 0, 0], [0, 1, 2], [0, 2, 4]]`

### Iterar sobre listas anidadas:
```python
lista_anidada = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for sublista in lista_anidada:
    for elemento en sublista:
        print(elemento)
```

---

## Conclusión

Las sentencias de control en Python (`if`, `while`, `for`) permiten manejar la lógica y el flujo de ejecución de los programas. El uso adecuado de estas, junto con funciones como `range()`, posibilita la manipulación eficiente de datos y la solución de problemas más complejos a través de bucles anidados y control de flujo.

| **Sentencia**   | **¿Qué hace?**                                     | **¿Cuándo usar?**                                                  |
|-----------------|----------------------------------------------------|--------------------------------------------------------------------|
| `if`            | Evalúa una condición y ejecuta un bloque de código. | Para decisiones condicionales (si algo es verdadero o falso).      |
| `while`         | Repite un bloque de código mientras una condición es verdadera. | Cuando necesitas repetir algo indefinidamente hasta que cambie la condición. |
| `for`           | Itera sobre una secuencia (listas, cadenas, etc.).  | Para recorrer colecciones o repetir una tarea un número específico de veces. |
| `range()`       | Genera una secuencia de números.                    | Para controlar bucles con un rango de valores.                     |
| `break`         | Interrumpe un bucle antes de que termine.           | Para salir de bucles en condiciones específicas.                   |
| Bucles anidados | Un bucle dentro de otro bucle.                      | Para trabajar con estructuras complejas (matrices, listas anidadas).|


