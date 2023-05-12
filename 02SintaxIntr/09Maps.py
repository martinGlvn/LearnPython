# Maps => Transformaciones de una lista de elementos.

numeros = [1, 2, 3, 4, 5]
numerosV2 = []

# Transformacion sin map
for x in numeros:
    numerosV2.append(x*2)
print(numerosV2)  # [2, 4, 6, 8, 10]

# Transformacion con map
numerosV3 = list(map(lambda x: x*2, numeros))
print(numerosV3)  # [2, 4, 6, 8, 10]

# Transformando 2 listas ---------------------------------------------
numero1 = [1, 2, 3, 4]
numero2 = [5, 6, 7, 8, 9, 10]
resultado = list(map(lambda x, y: x + y, numero1, numero2))
print(resultado)  # [6, 8, 10, 12]


# Maps con diccionarios ---------------------------------------------
