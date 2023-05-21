# Bucles => For

# Ejemplo =>
for i in range(0, 10):
    print(i)

# Ejemplo =>
for i in range(0, 99):
    print(i)

# Ejemplo=>
for i in range(5, 15):
    print(i)

# For => "Rango de Continuacion"
for i in range(0, 10, 2):
    print(i)  # 0 2 4 6 8

# For => "Rango de Retroceso"
for i in range(10, 2, -2):
    print(i)  # 10 8 6 4

# Ejemplo ->
for i in range(10, 1, -1):
    print(i)  # 10 9 8 7 6 5 4 3 2


# Imprimir variables en un string =>
num_bananas = 10
print(f"You have {num_bananas} bananas")  # You have 10 bananas

# Ejemplo =>
for age in range(0, 75):
    if age < 8:
        print("Usted califica para comidas gratis. Tienes EDAD años.")
    elif age > 65:
        print("Usted califica para la jubilación. Tienes EDAD años.")

# Ejemplo =>
total = 0
for i in range(0, 100):
    total += i
print(total)


# Ejemplo =>
for i in range(10, 0, -1):
    if i == 1:
        print("NUM... Blastoff!")
    else:
        print(i)

# Ejemplo =>
for i in range(100, 109):
    print(f"{i} squared = {i*i}")


# Ejemplo =>
number_of_employees = 102

c_level_bonus = 2000
manager_bonus = 1000
standard_bonus = 500

sarah_id = 1
mary_id = 2
john_id = 6
bob_id = 44
joe_id = 18
dollars_needed = 0

for i in range(0, number_of_employees - 1):
    if i == 1 or 2:
        dollars_needed += c_level_bonus
    elif i == 6 or 44 or 18:
        dollars_needed += manager_bonus
    else:
        dollars_needed += standard_bonus
print(f"{dollars_needed} dollars are needed to fulfill all bonuses")
