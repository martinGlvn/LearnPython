set_a = {'chile', 'uruguay', 'brasil'}
set_b = {'argentina', 'brasil', 'colombia'}

# Union de Conjuntos ->
set_c = set_a.union(set_b)
print(set_c)  # {'argentina', 'colombia', 'brasil', 'chile', 'uruguay'}
set_test = (set_a | set_b)
print(set_test)  # {'argentina', 'colombia', 'brasil', 'chile', 'uruguay'}

# Interseccion de Conjuntos -> "lo que se repite en los conjuntos"
set_z = set_a.intersection(set_b)
print(set_z)  # {'brasil'}
print(set_a & set_b)  # otra forma de hacer lo mismo -> {'brasil'}

# Diferencia de conjuntos ->
set_m = set_a.difference(set_b)
print(set_m)  # {'chile', 'uruguay'}
print(set_a - set_b)  # otra forma de hacer lo mismo -> {'chile', 'uruguay'}

# Diferencia Simetrica -> Union sin los elementos que coinciden en comun
set_w = set_a.symmetric_difference(set_b)
print(set_w)  # {'uruguay', 'argentina', 'chile', 'colombia'}
print(set_a ^ set_b)  # {'chile', 'colombia', 'argentina', 'uruguay'}
