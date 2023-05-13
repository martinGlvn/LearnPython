# Crear una función que dibuja un rombo según el número de filas dado

def dibujar_rombo(filas):
    # Parte superior del rombo
    for i in range(1, filas+1):  # Iteramos desde el rango 1 hasta x "numero por parametro"
        print(' '*(filas-i) + '° '*(i))
    # Parte inferior del rombo
    for i in range(filas-1, 0, -1):  # Iteramos desde el rango 1 hasta x "numero por parametro"
        print(' '*(filas-i) + '° '*(i))  # Centramos el rombo -


dibujar_rombo(8)
