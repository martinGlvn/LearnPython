a = input("Ingre una palabra: ")
v = "aeiou"
z = 0


c_vocales = {vocal: a.lower().count(vocal) for vocal in v}
for vocal, contador in c_vocales.items():
    z += 1
print(z, "vocales totales")


# Solucion pasar el dict a list
