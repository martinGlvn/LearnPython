def numPrimos(x, z):
    # lista de almacenamiento
    a = []

    for num in range(x, z + 1):
        # siempre que sea 2 o + entra a la condicion
        if num > 1:
            for i in range(2, int(num ** 0.5) + 1):
                if (num % i) == 0:
                    break
            else:
                a.append(num)
    return a


# Numeros generados
a = numPrimos(1, 250)

with open('primos.txt', 'w') as archivo:
    archivo.write('\n'.join(map(str, a)))
