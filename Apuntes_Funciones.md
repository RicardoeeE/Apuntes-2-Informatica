# Apuntes sobre Funciones en Python

## 1. Introducción a las Funciones

Las funciones son bloques de código reutilizables que realizan una tarea específica. Ayudan a organizar y modularizar el código.

### Beneficios de Usar Funciones:
- **Reutilización**: Puedes llamar a la misma función múltiples veces sin repetir el código.
- **Modularidad**: Facilitan la organización del código en partes más manejables.
- **Abstracción**: Permiten ocultar la complejidad y exponer solo la interfaz necesaria.

---

## 2. Definición de Funciones

### Sintaxis:
```python
def nombre_funcion(parametros):
    # código a ejecutar
    return valor_de_retorno
```

### Ejemplo:
```python
def suma(a, b):
    return a + b

resultado = suma(5, 3)
print(resultado)  # Salida: 8
```

### Casos de uso:
- Realizar cálculos repetitivos.
- Procesar datos.
- Implementar lógica de negocio.

---

## 3. Parámetros y Argumentos

### Parámetros:
Son variables que se definen en la función para recibir valores.

### Argumentos:
Son los valores que se pasan a la función al llamarla.

### Ejemplo:
```python
def multiplicar(a, b=2):  # 'b' tiene un valor por defecto
    return a * b

print(multiplicar(5))     # Salida: 10
print(multiplicar(5, 3))  # Salida: 15
```

### Tipos de Parámetros:
- **Posicionales**: Se pasan en el orden definido.
- **Por defecto**: Tienen un valor predeterminado si no se proporciona un argumento.
- **Arbitrarios**: Permiten pasar un número variable de argumentos.

### Ejemplo de parámetros arbitrarios:
```python
def sumar_todos(*numeros):  # '*' permite un número variable de argumentos
    return sum(numeros)

print(sumar_todos(1, 2, 3, 4))  # Salida: 10
```

---

## 4. Funciones Lambda

Las funciones lambda son funciones pequeñas y anónimas que se definen en una sola línea. Se utilizan para operaciones simples.

### Sintaxis:
```python
lambda argumentos: expresión
```

### Ejemplo:
```python
suma = lambda x, y: x + y
print(suma(5, 3))  # Salida: 8
```

### Casos de uso:
- Funciones de una sola línea.
- Como argumentos en funciones de orden superior (map, filter, etc.).

---

## 5. Alcance de las Variables

### Alcance Local:
Las variables definidas dentro de una función son locales a esa función y no son accesibles fuera de ella.

### Alcance Global:
Las variables definidas fuera de cualquier función son globales y pueden ser accedidas dentro de cualquier función.

### Ejemplo:
```python
x = 10  # Variable global

def mostrar():
    x = 5  # Variable local
    print(x)

mostrar()  # Salida: 5
print(x)   # Salida: 10
```

### Uso de la palabra clave `global`:
Se puede usar `global` para modificar una variable global dentro de una función.
```python
def cambiar_global():
    global x
    x = 20

cambiar_global()
print(x)  # Salida: 20
```

---

## 6. Documentación de Funciones

Es importante documentar las funciones usando cadenas de documentación (docstrings) para describir su propósito y uso.

### Sintaxis:
```python
def funcion():
    """
    Descripción de la función.
    """
    pass
```

### Ejemplo:
```python
def dividir(a, b):
    """
    Divide dos números y devuelve el resultado.
    
    Parámetros:
    a (int): El numerador.
    b (int): El denominador.
    
    Retorna:
    float: Resultado de la división.
    """
    return a / b
```

---

## 7. Ejemplo Completo

```python
def calcular_area_rectangulo(base, altura):
    """
    Calcula el área de un rectángulo.
    
    Parámetros:
    base (float): La base del rectángulo.
    altura (float): La altura del rectángulo.
    
    Retorna:
    float: El área del rectángulo.
    """
    return base * altura

area = calcular_area_rectangulo(5, 3)
print(f"El área del rectángulo es: {area}")  # Salida: El área del rectángulo es: 15
```

---

## Conclusión

Las funciones son una parte fundamental de la programación en Python. Permiten la reutilización del código, modularidad y claridad en el desarrollo. Con el uso adecuado de parámetros, argumentos y documentación, las funciones se convierten en herramientas poderosas para construir aplicaciones robustas y mantenibles.
```