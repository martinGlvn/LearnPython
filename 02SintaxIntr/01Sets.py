# Sets -> Se pueden modificar, no tienen orden, no tienen elementos duplicados
primerSet = {'arg', 'bol', 'peru'}
print(primerSet)

# Crear conjunto a partir de un "string" =>
setString = set("MARTIN")
print(setString)  # {'N', 'T', 'I', 'M', 'R', 'A'}

# Crear conjunto a partir de una "tupla" =>
setTuples = set(("abc", "zxd", "lkj"))
print(setTuples)  # {'lkj', 'zxd', 'abc'}

# Crear un conjunto a partir de una lista
numeros = [1, 2, 2, 4, 4, 10, 1]
setNumbers = set(numeros)
print(setNumbers)  # {1, 2, 10, 4}


# Modificando Conjuntos => CRUD

set_paises = {'arg', 'mx', 'col'}

print(len(set_paises))  # 3
print('peru' in set_paises)  # False

# add -> agrega elemento
set_paises.add("peru")
print(set_paises)  # {'col', 'arg', 'mx', 'peru'}

# update -> agrega conjuntos
set_paises.update({'chile', 'ecuador'})
print(set_paises)  # {'col', 'peru', 'arg', 'mx', 'chile', 'ecuador'}

# delete -> elimina elementos del conjunto
set_paises.remove('peru')
print(set_paises)  # {'mx', 'chile', 'arg', 'ecuador', 'col'}


set_paises.discard('italia')  # discard si el elemento no existe no daria error

set_paises.clear()  # elimina todo nuestro conjunto
print(set_paises)  # set() -> conjunto vacio ya que lo eliminamos.
