# Listas =>
# Un array no es lo mismo que una lista si bien ambas almacenan datos una lista
# posee metodos como reverse, insert, len, en cambio un array no tiene estos metodos.


# list
autos = list()
autos = ["jeje", "juju"]
print(len(autos))  # 2
print(autos.count(2))
autos.append("jojo")
print(autos)  # ['jeje', 'juju', 'juju']
autos.insert(0, "jaja")
print(autos)  # ['jaja', 'jeje', 'juju', 'juju']
autos.pop()
print(autos)  # ['jaja', 'jeje', 'juju']

# array
autosList = ["hola", "martin", 5]
print(autosList)  # ['hola', 'martin', 5]
print(autosList[0])  # hola
print(autosList[1])  # martin
print(autosList[-1])  # 5


#
