# Listas =>

numeros = [1, 2, 3, 4, 5]
print(numeros)

tareas = ["cocinar", "lavar"]
print(tareas)

# Posiciones en listas =>
posListas = ["hola", "chau"]
print(posListas[0])  # hola

# Modificar Listas
cursos = ["maths", "js"]
cursos[0] = "quantic"
print(cursos)  # ['quantic', 'js']

# SlicingListas
numeros2 = [10, 20, 50, 100]
print(numeros2[:2])  # [10, 20]

# Verificar el dato en una lista
autos = ["red", "blue"]
print("red" in autos)  # True


# Metodos en Listas =>

futbol = ["boca", "river", "racing"]

# CRUD ->
print(futbol)
futbol[0] = "independiente"
print(futbol)  # ['independinente', 'river', 'racing']
futbol.append("boca")
print(futbol)  # ['independiente', 'river', 'racing', 'boca']
futbol.insert(3, "mineiro")
print(futbol)  # ['independiente', 'river', 'racing', 'mineiro', 'boca']

# Unificando listas
comidas = ["pizza", "asado"]
bebidas = ["coca", "pepsi"]
comidasBebidas = comidas + bebidas
print(comidasBebidas)  # ['pizza', 'asado', 'coca', 'pepsi']

# Consultar posicion de un elemento y modificar
testPosition = ["noche", "dia", "mañana"]
consultIndex = testPosition.index("noche")
testPosition[consultIndex] = "tarde"
print(testPosition)  # ['tarde', 'dia', 'mañana']

# Remover elementos de nuestra lista
testList = ["task", "work"]
testList.remove("task")
print(testList)  # ["work"]

# Remover el ultimo elemento de nuestra lista
testList2 = ["jeje", "jaja"]
testList2.pop()
print(testList2)  # ['jeje']

# Invertir todo el contenido de nutra lista -> "REVERSE"
testList3 = ["hermana", "hermano", "tio"]
testList3.reverse()
print(testList3)  # ['tio', 'hermano', 'hermana']

# Ordenar nuestra lista -> "SORT"
testNumbers = [1, 5, 2, 4, 3]
testNumbers.sort()
print(testNumbers)  # [1, 2, 3, 4, 5]

testStrings = ["ac", "ab", "ad"]
testStrings.sort()
print(testStrings)  # ['ab', 'ac', 'ad']
