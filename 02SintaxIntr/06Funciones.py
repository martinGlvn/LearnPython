# Funciones --------------------------------------------------
def firstFunction():
    print("primeraFuncion")


firstFunction()  # primeraFuncion


# Funcion 2 --------------------------------------------------
def firstFunction2(texto):
    print("primeraFuncion", texto*2)


firstFunction2("hola")  # primeraFuncion holahola


# Funcion suma --------------------------------------------------
def sum(a, b):
    print(a+b)


sum(5, 10)  # 15


# Funciones -> Return -------------------------------------------
def sum_range(min, max):
    sum = 0
    for x in range(min, max):
        sum += x
    return sum


result = sum_range(5, 10)
print(result)  # 35
utilizandoResult = sum_range(result, result+10)
print(utilizandoResult)  # 395


# Funciones -> valores x defecto ----------------------------------
def volumen(a=1, b=1, c=1):
    return "tu volumen es", a*b*c


texto, resultado = volumen(5, 10, 50)
print(resultado)  # ('tu volumen es', 2500)
print(texto)


# Scope Funciones  ----------------------------------   
