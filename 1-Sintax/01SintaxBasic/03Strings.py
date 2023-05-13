# String =>
nombre = "martin"
estado = "none"

print(nombre)
print(estado)
print(nombre + " " + estado)

# Salto de linea en strings =>
saltoLinea = "Este es un salto de \n linea"
print(saltoLinea)

# Tabulacion en strings =>
tabulacion = "\tEste es un string con tabulacion al inicio"
print(tabulacion)

# Creacion de multiples strings =>
marca, auto,  año = "Mercedes Benz", "GT50", 1975
print(auto)
print(marca)
print(año)

# Concatenation de strings con variables =>
print("El %s modelo %s es muy rapido a pesar de ser del año %d" % (marca, auto, año))
print(f"El {marca} modelo {auto} es muy rapido a pesar de ser del año {año}")

# Desgloze de letras - caracteres en strings =>
code = "python"
a, b, c, d, e, f = code
print(a, b)  # py

# Dividiendo string por longitud =>
code2 = "JavaScript"
otroLenguaje = code2[0:4]
print(otroLenguaje)  # Java

finalCode = code2[4:]
print(finalCode)  # Script

# Codigo en reversa =>
reverseCode = code2[::-1]
print(reverseCode)  # tpircSavaJ


# Operadores en strings =>
text2 = "Hola Universo como andamo"

print("hola" in text2)  # True
print(len(text2))  # 13
print(text2.upper())  # HOLA UNIVERSO
print(text2.lower())  # hola universo
print(text2.count('a'))  # 1
print(text2.swapcase())  # hOLA uNIVERSO
print(text2.startswith('Hola'))  # True
print(text2.endswith('Universo'))  # True
print(text2.replace('Hola', 'Chau'))  # Chau Universo
print(text2.capitalize())  # Hola universo
print(text2.title())  # Hola Universo Como Andamo
print(text2.isdigit())  # False

# Indices
textoIndices = "Estamos estudiando Python"
print(textoIndices[0])  # E
print(textoIndices[-1])  # n

# Slicing
recortartarTexto = "Este texto vamos a recortar"
print(recortartarTexto[:19])  # Este texto vamos a
print(recortartarTexto[5:])  # texto vamos a recortar
