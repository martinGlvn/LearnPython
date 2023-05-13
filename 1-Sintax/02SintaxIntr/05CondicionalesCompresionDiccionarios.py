import random

# CondicionalesCompresionDiccionarios


# Creamos un diccionario con popularidad > a 20 x pais
paises = ['col', 'arg', 'peru']
popularidad = {a: random.randint(1, 100) for a in paises}
resultado = {pais: popularidad for (
    pais, popularidad) in popularidad.items() if popularidad > 20}
print(resultado)  # {'col': 60, 'arg': 29, 'peru': 50}

# Creamos un diccionario con clave y valor de las vocales de un texto.
texto = "Hola como andamos"
valores = {a: a.upper() for a in texto if a in 'aeiou'}
print(valores)  # {'o': 'O', 'a': 'A'}
