""""EJERCICIO 1: Un estudiante está cursando 5 materias, tiene la nota de cada

materia y quiere saber cuál es su promedio.

"""

# Definimos una lista para almacenar las notas de las materias
notas = []

# Solicitamos al usuario que ingrese las notas de las 5 materias
for i in range(1, 6):
    nota = float(input(f"Ingrese la nota de la materia {i}: "))
    notas.append(nota)

# Calculamos el promedio
promedio = sum(notas) / len(notas)

# Mostramos el promedio al usuario
print(f"El promedio de las notas es: {promedio}")
