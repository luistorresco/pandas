# Análisis de Datos de Estudiantes

Este proyecto genera y analiza un conjunto de datos aleatorios de estudiantes, incluyendo información sobre sus nombres, apellidos, edades, asignaturas y notas. A continuación, se presentan las preguntas y respuestas derivadas del análisis de estos datos.

## Preguntas y Respuestas

1. **¿Cuál es la edad promedio de los estudiantes?**
    - La edad promedio de los estudiantes es: `edad_promedio`.

2. **¿Quién es el estudiante más joven y cuál es su edad?**
    - El estudiante más joven es: `estudiante_mas_joven['nombre']` `estudiante_mas_joven['apellido']`.

3. **¿Quién es el estudiante más viejo y cuál es su edad?**
    - El estudiante más viejo es: `estudiante_mas_viejo['nombre']` `estudiante_mas_viejo['apellido']`.

4. **¿Cuáles son los nombres y apellidos de los estudiantes con las 10 notas más altas?**
    - Los estudiantes con las 10 notas más altas son:
    ```plaintext
    `estudiantes_notas_altas[['nombre', 'apellido', 'nota']]`
    ```

5. **¿Cuál es el número de estudiantes por asignatura?**
    - El número de estudiantes por asignatura es:
    ```plaintext
    `estudiantes_por_materia`
    ```

6. **¿Qué asignatura tiene la nota más alta y quién la obtuvo?**
    - La materia con la nota más alta es: `materia_nota_mas_alta`.

7. **¿Qué asignatura tiene la nota más baja y quién la obtuvo?**
    - La materia con la nota más baja es: `materia_nota_mas_baja`.

8. **¿Cuál es el promedio de las notas de los estudiantes?**
    - El promedio de notas de los estudiantes es: `promedio_notas`.

9. **¿Cuántos estudiantes han aprobado (nota >= 60) y cuántos han reprobado (nota < 60)?**
    - El número de estudiantes que ganan es: `estudiantes_ganan`.
    - El número de estudiantes que pierden es: `estudiantes_pierden`.

10. **¿Cuál es la nota más alta en Matemáticas y quién la obtuvo?**
    - La nota más alta en Matemáticas es: `nota_mas_alta_matematicas`.
    - El estudiante con la nota más alta en Matemáticas es: `estudiante_nota_mas_alta_matematicas['nombre'].values[0]` `estudiante_nota_mas_alta_matematicas['apellido'].values[0]`.

11. **¿Cuál es la nota más baja en Historia y quién la obtuvo?**
    - La nota más baja en Historia es: `nota_mas_baja_historia`.
    - El estudiante con la nota más baja en Historia es: `estudiante_nota_mas_baja_historia['nombre'].values[0]` `estudiante_nota_mas_baja_historia['apellido'].values[0]`.

12. **¿Cuántos estudiantes están en el rango de edad de 30 a 40 años?**
    - El número de estudiantes en el rango de 30 a 40 años es: `estudiantes_rango_edad`.

## Generación de Datos

El conjunto de datos se genera mediante la función `generate_data()`, que crea un DataFrame con los siguientes campos:
- `nombre`
- `apellido`
- `edad`
- `asignatura`
- `nota`

## Uso

1. Clona este repositorio.
2. Ejecuta el script para generar el archivo CSV con los datos de los estudiantes.
3. Utiliza el análisis proporcionado para responder las preguntas anteriores.

```python
import pandas as pd
import numpy as np

def generate_data():
    """
    Genera un DataFrame con datos aleatorios de estudiantes.

    Returns:
        pandas.DataFrame: Un DataFrame con columnas 'nombre', 'apellido', 'edad', 'asignatura' y 'nota'.
            La columna 'nombre' contiene nombres aleatorios.
            La columna 'apellido' contiene apellidos aleatorios.
            La columna 'edad' contiene edades aleatorias entre 18 y 25.
            La columna 'asignatura' contiene nombres aleatorios de asignaturas.
            La columna 'nota' contiene notas aleatorias entre 60 y 100.
    """
    nombres = ['Juan', 'María', 'José', 'Ana', 'Pedro', 'Luisa', 'Carlos', 'Laura', 'Miguel', 'Sofía']
    apellidos = ['García', 'Rodríguez', 'Martínez', 'Hernández', 'López', 'González', 'Pérez', 'Sánchez', 'Ramírez', 'Torres']
    asignaturas = ['Matemáticas', 'Física', 'Química', 'Historia', 'Literatura', 'Biología', 'Inglés', 'Arte', 'Música', 'Economía']

    data = {
        'nombre': np.random.choice(nombres, size=100),
        'apellido': np.random.choice(apellidos, size=100),
        'edad': np.random.randint(18, 26, size=100),
        'asignatura': np.random.choice(asignaturas, size=100),
        'nota': np.random.randint(60, 101, size=100)  # Notas entre 60 y 100
    }
    return pd.DataFrame(data)

# Generar los datos
data = generate_data()

# Guardar los datos en un archivo CSV
data.to_csv('datos.csv', index=False)

print("Se han generado y guardado los datos en 'datos.csv'.")
