# Empresa de transporte requiere guardar el nombre y recorido de cada conductor
# Para guardar esta informacion se utilizaran dos arrays
# NOMBRE = []
# KMS = []
# Se quiere generar una nueva lista ('total_kms') con los kilometros
# totales que realiza cada conductor.
# Lista de nombres de los conductores
conductores = []
i = input("indique la cantidad de conductores: ")
for x in i:
    nombre = input("indique nombre del conductor ", i, ": ")
    conductores.append[nombre]

for x in i:
    kilometros = float(
        input("Indique la cantidad de kilometros recorridos por ", conductores[i], ": "))

total_kms = []


for i in range(len(nombre)):
    total = 0

    for j in range(len(kilometros[i])):
        total += kilometros[i][j]
    total_kms.append(total)

# Mostramos los nombres de los conductores y los kilometros totales que han recorrido
for i in range(len(nombre)):
    print(nombre[i] + " ha recorrido " +
          str(total_kms[i]) + " kilometros en total.")
# Cond1 = []
# CondTotal = [Cond1, Cond2, Cond3]
# CondTotal = 1, 2, 3
# Cond1= [J , 10 20 30, 60]
