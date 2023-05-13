# While ->
contador = 0
while contador < 10:
    contador += 1
    print(contador)

# While if ->
condicion = 0
while condicion < 10:
    print(condicion)
    condicion += 2
else:
    print("es mayor o igual a 10")


# Break
contador2 = 0
while contador2 < 20:
    contador2 += 1
    if contador2 == 15:
        break
    print(contador2)

# Continue
contador3 = 0
while contador3 < 20:
    contador3 += 1
    if contador3 < 15:
        continue
    print(contador3)


# For ->

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for anashe in lista:
    print(anashe)

# For en Diccionario ->
diccionario = {"nombre": "martin", "edad": 50}
for miInfo in diccionario.values():
    print(miInfo)

# For y break ->
for info in diccionario.values():
    print(info)
    if info == "martin":
        break
else:
    print("seguimos")

# Ciclos Anidaods ->

x = 10
b = 10


def suma():
    print(x+b)


suma()
