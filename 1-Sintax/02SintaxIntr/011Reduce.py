# Reduce => reducir el tamaño de una lista.
import functools
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# utilizando reduce
r = functools.reduce(lambda counter, item: counter + item, numeros)
print(r)  # 55

# sin utilizar reduce


def ac(counter, item):
    print(counter)
    print(item)
    return counter + item


resultado = functools.reduce()
