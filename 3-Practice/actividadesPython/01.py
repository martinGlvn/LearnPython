# 1. Escribir un programa que almacene las asignaturas de un curso
# (por ejemplo Matematicas, Fisica, Quimica, Historia y Lengua) en una lista
# pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la lista las asignaturas aprobadas.
# Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir.

materias = ["Matematicas", "Fisica", "Quimica", "Historia", "Lengua"]
notas = []

# Consulta de notas x materias =>
for x in materias:
    nota = int(input("Que nota te sacaste en " + x))
    notas.append(nota)

print(notas)

# Almacenamos las Materias desaprobadas en un array nuevo.
materiasDesaprobadas = []
for z in range(len(materias)):
    if notas[z] > 5:
        print("Aprobaste")
        print("Se elimina la materia: " + materias[z])
    else:
        materiasDesaprobadas.append(materias[z])

print("Las materias que debe repetir son: " + str(materiasDesaprobadas))
