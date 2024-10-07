# Apuntes sobre NumPy en Python

## 1. Introducción a NumPy

NumPy es una biblioteca fundamental para la computación científica en Python. Proporciona un objeto de matriz multidimensional, así como funciones para realizar operaciones sobre estas matrices de manera eficiente.

### Beneficios de Usar NumPy:
- **Eficiencia**: Las operaciones sobre arreglos de NumPy son más rápidas que las de listas de Python.
- **Funcionalidad**: Ofrece una amplia gama de funciones matemáticas y lógicas.
- **Interoperabilidad**: Compatible con otras bibliotecas como SciPy, Pandas, y Matplotlib.

---

## 2. Instalación

Para instalar NumPy, puedes utilizar `pip`:

```bash
pip install numpy
```

---

## 3. Creación de Arreglos

NumPy proporciona diversas formas de crear arreglos:

### 3.1. Crear un Arreglo a partir de una Lista

```python
import numpy as np

arreglo = np.array([1, 2, 3, 4, 5])
print(arreglo)  # Salida: [1 2 3 4 5]
```

### 3.2. Crear Arreglos de Ceros y Unos

```python
ceros = np.zeros((2, 3))  # Matriz de ceros de 2x3
print(ceros)
# Salida:
# [[0. 0. 0.]
#  [0. 0. 0.]]

unos = np.ones((2, 3))  # Matriz de unos de 2x3
print(unos)
# Salida:
# [[1. 1. 1.]
#  [1. 1. 1.]]
```

### 3.3. Crear un Arreglo de Números Aleatorios

```python
aleatorios = np.random.rand(3, 2)  # Matriz de 3x2 con números aleatorios
print(aleatorios)
```

### 3.4. Crear un Arreglo con un Rango de Números

```python
rango = np.arange(10)  # Arreglo con valores del 0 al 9
print(rango)  # Salida: [0 1 2 3 4 5 6 7 8 9]

rango_con_pasos = np.arange(0, 10, 2)  # Rango con pasos de 2
print(rango_con_pasos)  # Salida: [0 2 4 6 8]
```

### 3.5. Crear una Matriz Identidad

```python
identidad = np.eye(3)  # Matriz identidad de 3x3
print(identidad)
# Salida:
# [[1. 0. 0.]
#  [0. 1. 0.]
#  [0. 0. 1.]]
```

---

## 4. Propiedades de los Arreglos

### 4.1. Dimensiones y Forma

Puedes consultar la dimensión y la forma de un arreglo:

```python
arreglo = np.array([[1, 2, 3], [4, 5, 6]])
print(arreglo.shape)  # Salida: (2, 3) - 2 filas y 3 columnas
print(arreglo.ndim)   # Salida: 2 - número de dimensiones
print(arreglo.size)   # Salida: 6 - número total de elementos
```

---

## 5. Indexación y Slicing

NumPy permite acceder y modificar elementos de los arreglos de manera eficiente.

### 5.1. Indexación

```python
arreglo = np.array([1, 2, 3, 4, 5])
print(arreglo[0])  # Salida: 1
print(arreglo[-1]) # Salida: 5
```

### 5.2. Slicing

```python
arreglo = np.array([1, 2, 3, 4, 5])
print(arreglo[1:4])  # Salida: [2 3 4]

matriz = np.array([[1, 2, 3], [4, 5, 6]])
print(matriz[:, 1])  # Salida: [2 5] - segunda columna
print(matriz[1, :])  # Salida: [4 5 6] - segunda fila
```

### 5.3. Modificación

```python
matriz[0, 0] = 10
print(matriz)  # Salida: [[10  2  3]
                #          [ 4  5  6]]
```

---

## 6. Operaciones Aritméticas

NumPy permite realizar operaciones aritméticas de manera eficiente y en paralelo.

### 6.1. Suma, Resta, Multiplicación y División

```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(a + b)  # Salida: [5 7 9]
print(a - b)  # Salida: [-3 -3 -3]
print(a * b)  # Salida: [ 4 10 18]
print(a / b)  # Salida: [0.25 0.4  0.5 ]
```

### 6.2. Operaciones Element-wise

NumPy permite operaciones element-wise sin necesidad de bucles.

```python
a = np.array([[1, 2], [3, 4]])
b = np.array([[10, 20], [30, 40]])

print(a + b)  # Salida: [[11 22]
               #          [33 44]]

print(a * 2)  # Multiplicación por escalar
# Salida: [[2 4]
#          [6 8]]
```

### 6.3. Funciones Matemáticas

```python
arreglo = np.array([1, 4, 9])
print(np.sqrt(arreglo))  # Raíz cuadrada de cada elemento
# Salida: [1. 2. 3.]

print(np.exp(arreglo))  # Exponencial de cada elemento
# Salida: [  2.71828183  54.59815003 8103.08392758]
```

---

## 7. Funciones Agregadas

NumPy proporciona funciones para realizar cálculos sobre arreglos.

### 7.1. Sumar y Promediar

```python
arreglo = np.array([[1, 2, 3], [4, 5, 6]])

print(np.sum(arreglo))          # Salida: 21
print(np.sum(arreglo, axis=0))  # Suma por columnas
# Salida: [5 7 9]
print(np.mean(arreglo))         # Salida: 3.5
```

### 7.2. Mínimo y Máximo

```python
print(np.min(arreglo))  # Salida: 1
print(np.max(arreglo))  # Salida: 6
```

### 7.3. Desviación Estándar

```python
print(np.std(arreglo))  # Salida: 1.707825127659933
```

---

## 8. Manipulación de Arreglos

### 8.1. Reshape

Puedes cambiar la forma de un arreglo sin cambiar sus datos.

```python
arreglo = np.array([1, 2, 3, 4, 5, 6])
nuevo_arreglo = arreglo.reshape(2, 3)
print(nuevo_arreglo)
# Salida:
# [[1 2 3]
#  [4 5 6]]
```

### 8.2. Transponer

```python
matriz = np.array([[1, 2, 3], [4, 5, 6]])
print(matriz.T)
# Salida:
# [[1 4]
#  [2 5]
#  [3 6]]
```

### 8.3. Concatenar y Dividir

```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Concatenar
concatenado = np.concatenate((a, b))
print(concatenado)  # Salida: [1 2 3 4 5 6]

# Dividir
c = np.array([[1, 2, 3], [4, 5, 6]])
dividido = np.split(c, 2)  # Divide en 2 partes
print(dividido)  # Salida: [array([[1, 2, 3]]), array([[4, 5, 6]])]
```

---

## 9. Bucles en NumPy

Aunque NumPy permite operaciones vectorizadas, en algunas ocasiones es necesario iterar sobre los elementos.

### Ejemplo de bucle:

```python
arreglo = np.array([1, 2, 3, 4, 5])
for i in arreglo:
    print(i * 2)  # Salida: 2, 4, 6, 8, 10
```



Sin embargo, es preferible utilizar funciones de NumPy en lugar de bucles siempre que sea posible.

---

## 10. Visualización con Matplotlib

NumPy se integra bien con Matplotlib para visualización de datos.

### Ejemplo:

```python
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100)  # 100 puntos entre 0 y 10
y = np.sin(x)

plt.plot(x, y)
plt.title('Seno de x')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.grid()
plt.show()
```

---

## Conclusión

NumPy es una herramienta esencial para la manipulación y análisis de datos en Python. Su eficiencia y versatilidad la convierten en la elección preferida para muchos científicos de datos y programadores. Aprender a utilizar NumPy abre la puerta a un mundo de posibilidades en la computación científica y el análisis de datos.
```