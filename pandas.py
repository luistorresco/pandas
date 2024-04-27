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
# Calcular la edad promedio de los estudiantes
edad_promedio = data['edad'].mean()
print("La edad promedio de los estudiantes es:", edad_promedio)

# Encontrar el estudiante más joven
estudiante_mas_joven = data.loc[data['edad'].idxmin()]

# Encontrar el estudiante más viejo
estudiante_mas_viejo = data.loc[data['edad'].idxmax()]

# Imprimir los resultados
print("El estudiante más joven es:", estudiante_mas_joven['nombre'], estudiante_mas_joven['apellido'])
print("El estudiante más viejo es:", estudiante_mas_viejo['nombre'], estudiante_mas_viejo['apellido'])

# Encontrar los estudiantes con las 10 notas más altas
estudiantes_notas_altas = data.nlargest(10, 'nota')
print("Los estudiantes con las 10 notas más altas son:")
print(estudiantes_notas_altas[['nombre', 'apellido', 'nota']])

estudiantes_por_materia = data['asignatura'].value_counts()
print("El número de estudiantes por materia es:")
print(estudiantes_por_materia)

# Encontrar la materia con la nota más alta
materia_nota_mas_alta = data.loc[data['nota'].idxmax()]['asignatura']

# Encontrar la materia con la nota más baja
materia_nota_mas_baja = data.loc[data['nota'].idxmin()]['asignatura']

print("La materia con la nota más alta es:", materia_nota_mas_alta)
print("La materia con la nota más baja es:", materia_nota_mas_baja)

promedio_notas = data['nota'].mean()
print("El promedio de notas de los estudiantes es:", promedio_notas)

# Contar cuántos estudiantes ganan y cuántos pierden
estudiantes_ganan = len(data[data['nota'] >= 60])
estudiantes_pierden = len(data[data['nota'] < 60])

print("El número de estudiantes que ganan es:", estudiantes_ganan)
print("El número de estudiantes que pierden es:", estudiantes_pierden)

# Encontrar la nota más alta en matemáticas y quién la tiene
nota_mas_alta_matematicas = data.loc[data['asignatura'] == 'Matemáticas', 'nota'].max()
estudiante_nota_mas_alta_matematicas = data.loc[(data['asignatura'] == 'Matemáticas') & (data['nota'] == nota_mas_alta_matematicas)]

print("La nota más alta en Matemáticas es:", nota_mas_alta_matematicas)
print("El estudiante con la nota más alta en Matemáticas es:", estudiante_nota_mas_alta_matematicas['nombre'].values[0], estudiante_nota_mas_alta_matematicas['apellido'].values[0])

nota_mas_baja_historia = data.loc[data['asignatura'] == 'Historia', 'nota'].min()
estudiante_nota_mas_baja_historia = data.loc[(data['asignatura'] == 'Historia') & (data['nota'] == nota_mas_baja_historia)]

print("La nota más baja en Historia es:", nota_mas_baja_historia)
print("El estudiante con la nota más baja en Historia es:", estudiante_nota_mas_baja_historia['nombre'].values[0], estudiante_nota_mas_baja_historia['apellido'].values[0])

estudiantes_rango_edad = len(data[(data['edad'] >= 30) & (data['edad'] <= 40)])
print("El número de estudiantes en el rango de 30 a 40 años es:", estudiantes_rango_edad)
