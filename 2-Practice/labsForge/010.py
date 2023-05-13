# La limpieza de archivos de datos iniciales es una tarea común en programación.
# Puede realizar la limpieza de preproinsulin-seq.txt mediante programación de varias
# formas, por ejemplo, con el uso de Bash, Python u otro lenguaje de programación de su elección.
# Pruebe utilizar expresiones regulares para eliminar mediante programación el archivo de ORIGIN,
# sus números, las dos barras diagonales (//), los espacios y los saltos de línea o los carros de retorno.
# También puede confirmar mediante programación que el archivo tiene 110 caracteres.

with open('preproinsulin-seq.txt', 'r') as archivo:
    contenido = archivo.read()

print(contenido)

eliminoDatos = ["ORIGIN", " ", "//"]

for datos in eliminoDatos:
    contenido = contenido.replace(datos, '')

print(contenido)

# 24 - 30 - 35 - 21
a = contenido[0:24]
b = contenido[24:54]
c = contenido[54:89]
d = contenido[89:110]

# contenido del archivo .txt


def create_file(filename):
    with open(filename, 'w') as file:
        file.write(a, b, c, d)


files = ["preproinsulin-seq-clean.txt",  "lsinsulin-seq-clean.txt",
         "binsulin-seq-clean.txt", "cinsulin-seq-clean.txt", "ainsulin-seq-clean.txt"]

# nombre de los archivos .txt
for file in files:
    create_file(file)
