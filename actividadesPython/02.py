# Queremos guardar la temperatura mínima y máxima de 5 días.
# Realiza un programa que de la siguiente información:
# La temperatura media de cada día
# Los días con menos temperatura
# Se lee una temperatura por teclado y se muestran los días cuya temperatura máxima coincide con ella.
# si no existe ningún día se muestra un mensaje de información.

temperaturas = []
temperaturaMediaDia = []

for i in range(1, 3):
    print("Ingrese las temperaturas para el dia " + str(i))
    minima = float(input("Temperatura minima es: "))
    maxima = float(input("Temperatura maxima es: "))
    temperaturas.append((minima, maxima))

    temperaturaMediaDia = float(minima + maxima)/2

print(temperaturas)

for i in temperaturaMediaDia:
    print("La temperatura media del dia %i " + temperaturaMediaDia)
