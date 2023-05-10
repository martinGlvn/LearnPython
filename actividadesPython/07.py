# Escribir un programa en el que se pregunte al usuario por una frase y una letra,
# y muestre por pantalla el número de veces que aparece la letra en la frase.


# pregunte al usuario = input -> frase y letra
# print = letras repetidas.

frase = input("Ingresa la frase : ")
letra = input("Ingresa una letra : ")

repeticionesFrase = 0

for x in frase:
    print(x)
    if x == letra:
        repeticionesFrase = repeticionesFrase + 1  # o += 1

print("En la frase", "'" + frase + "'",  "se repite : ", letra,
      repeticionesFrase, "cantidad de veces")
