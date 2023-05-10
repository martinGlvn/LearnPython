import random
# Compresion de Diccionarios

# sin compresion
diccionario = {}
for i in range(1, 5):
    diccionario[i] = i * 2
print(diccionario)  # {1: 2, 2: 4, 3: 6, 4: 8}

# con compresion
diccionarioV2 = {i: i*2 for i in range(1, 5)}
print(diccionarioV2)  # {1: 2, 2: 4, 3: 6, 4: 8}


# Diccionario y Array -> Sin crompresion
paises = ["arg", "peru", "chile"]
popularidad = {}
for a in paises:
    popularidad[a] = random.randint(1, 10)
print(popularidad)  # {'arg': 5, 'peru': 7, 'chile': 6}

# Diccionario y Array -> Con crompresion
popularidadV2 = {a: random.randint(1, 10) for a in paises}
print(popularidadV2)  # {'arg': 10, 'peru': 6, 'chile': 4}


# Generamos un lista a partir de 2 listas ->
nombres = ["martin", "nicolas", "santino"]
edades = [25, 21, 23]
print(list(zip(nombres, edades)))
# [('martin', 25), ('nicolas', 21), ('santino', 23)]


# Generamos un Diccionario a partir de 2 listas ->
nombres2 = ["agustin", "edgardo", "facundo"]
edades2 = [32, 55, 39]
dic = {nombre: edad for (nombre, edad) in zip(nombres2, edades2)}
print(dic)  # {'agustin': 32, 'edgardo': 55, 'facundo': 39}
