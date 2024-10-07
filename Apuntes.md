```markdown
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

---

## 2. Sentencia `while`

La sentencia `while` permite ejecutar un bloque de código repetidamente mientras una condición sea verdadera.

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

### Uso de `break`:
`break` permite terminar la ejecución de un bucle antes de que la condición sea falsa.
```python
i = 1
while True:
    print(i)
    i += 1
    if i > 5:
        break
```

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
```python
for i in range(10):
    if i == 5:
        break
    print(i)
```

---

## 4. El `in range`

La función `range()` genera una secuencia de números. Es muy útil para controlar bucles, especialmente con `for`.

### Sintaxis:
```python
range(start, stop, step)
```

- `start`: el valor inicial de la secuencia (opcional, por defecto es 0).
- `stop`: el valor donde se detiene (no incluye este valor).
- `step`: el incremento (opcional, por defecto es 1).

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

### Uso del `in` con `range`:
El `in` puede usarse para verificar si un número está en el rango generado.
```python
print(3 in range(1, 5))  # True porque 3 está en el rango 1-4
print(5 in range(1, 5))  # False porque 5 no está en el rango 1-4
```

---

## 5. Sentencias Iterativas Anidadas

Es posible anidar bucles dentro de otros bucles. Esto se utiliza cuando es necesario iterar sobre múltiples niveles de una estructura de datos o resolver problemas complejos.

### Sintaxis:
```python
for variable1 in secuencia1:
    for variable2 in secuencia2:
        # código a ejecutar en cada iteración anidada
```

### Ejemplo:
```python
for i in range(3):  # Bucle externo
    for j in range(2):  # Bucle interno
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
El `break` en un bucle anidado solo interrumpe el bucle en el que está ubicado.
```python
for i in range(3):
    for j in range(2):
        if j == 1:
            break
        print(f"i: {i}, j: {j}")
```

### Ejemplo de anidación con `while` y `for`:
```python
i = 0
while i < 3:
    for j in range(2):
        print(f"i: {i}, j: {j}")
    i += 1
```

---

## 6. Casos de uso comunes de `range` y bucles anidados

1. **Generar una matriz**:
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

2. **Iterar sobre listas anidadas**:
   ```python
   lista_anidada = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
   for sublista in lista_anidada:
       for elemento en sublista:
           print(elemento)
   ```

---

## Conclusión

Las sentencias de control en Python son herramientas fundamentales para la lógica de los programas. El uso adecuado de `if`, `while`, `for`, y `break` permite manejar una gran variedad de situaciones. Además, la función `range()` es esencial para manejar secuencias de números en bucles, y las sentencias anidadas permiten resolver problemas más complejos.
```

