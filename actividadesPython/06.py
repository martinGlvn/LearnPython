# Escribir un programa para una empresa que tiene salas de juegos para todas las edades y
# quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar.
# El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada.
# Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar 5€
# y si es mayor de 18 años, 10€.

edad1 = int(input("Cual es tu edad? "))

precio = 0 if edad1 < 4 else 5 if edad1 <= 18 else 10

print("El precio de entrada es:", precio, "€")

# if (edad1 < 4):
#     print("pase gratis")
# elif edad1 >= 4 and edad1 <= 18:
#     print("abonar 5 euros")
# else:
#     print("Debe abonar 10€")
