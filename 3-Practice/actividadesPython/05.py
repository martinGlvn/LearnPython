# Ejercicio 1- FINISH
renta = float(input("Ingrese su renta anual = $"))
tramos = [(10000, 0.05), (20000, 0.15), (35000, 0.20),
          (60000, 0.30), (float('inf'), 0.45)]
# (10000   ---   0.05)
# (20000   ---   0.15)
# (3500   ---   0.20)
for tramo, tipo_impositivo in tramos:
    if renta < tramo:
        print("Su pago impositivo correspondiente es:", tipo_impositivo*100, "%")
        break
