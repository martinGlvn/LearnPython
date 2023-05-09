# La limpieza de archivos de datos iniciales es una tarea común en programación. Puede realizar la limpieza de preproinsulin-seq.txt mediante programación de varias formas, por ejemplo, con el uso de Bash, Python u otro lenguaje de programación de su elección. Pruebe utilizar expresiones regulares para eliminar mediante programación el archivo de ORIGIN, sus números, las dos barras diagonales (//), los espacios y los saltos de línea o los carros de retorno. También puede confirmar mediante programación que el archivo tiene 110 caracteres.

with open('preproinsulin-seq.txt', 'r') as archivo:
    contenido = archivo.read()
    print(contenido)
