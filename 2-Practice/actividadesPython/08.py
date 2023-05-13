# Escribir un programa que pida al usuario un número entero y muestre por pantalla un
# triángulo rectángulo como el de más abajo.
# 1 -
# 3 3 1
# 57 5 31 3
# 7531
# 97531

# input -> numero entero
# numero entero ->

def getNumber():
    num = int(input("Put a number: "))
    return num


def drawATriangle():
    num = getNumber()
    for i in range(1, num+1):
        for j in range(i, 0, -1):
            print(j, end=" ")
        print()


drawATriangle()
