# Numeros Python =>

# suma
print(2 + 1)  # 3
# resta
print(2 - 1)  # 1
# multiplicacion
print(2 * 1)  # 2
# division
print(2 / 2)  # 1


#
sword_damage = 3
arrow_damage = 5
spear_damage = 2
dagger_damage = 1
fire_damage = 4
total_damage = sword_damage + arrow_damage + \
    spear_damage + dagger_damage + fire_damage
average_damage = total_damage / 7
print(f"total damage is: {total_damage}")
print(f"average damage is: {average_damage}")

# Numeros Enteros  & Numeros Flotantes =>
my_int = 5
my_float = 5.5

# Cociente de una division =>
print(7 // 3)  # 2

# Exponentes en python =>
print(3 ** 2)  # 9

# Mas igual en python =>
star_rating = 4
star_rating += 1
print(star_rating)  # 5

player_health = 156
player_health += 10
print(player_health)  # 166

# Notacion Cientifica =>
print(16e3)  # 16000.0
print(7.1e-2)  # 0.071
max_number_of_players = 1024E15
print(max_number_of_players)

# Guiones para facilitar la lectura =>
num = 16_000
print(num)  # 16000
num2 = 16_000_000
print(num)  # 16000000

# Binarios en python => "prefijo" 0b
print(0b0001)
print(0b0101)

# Operador bit a bit "&" =>
a = 0b0101
b = 0b0111
# -----0101 = 5

# Operador not => invierte nuestro resultado
print(not True)  # False

# Adicion Binaria =>
num_heads = 0b0001
num_arms = 0b1010
num_fingers = num_heads + num_arms
print(num_fingers)
# Desafios =>

num_fruit_bats = 8e6
num_male_bats = 3e6
ratio = num_male_bats / num_fruit_bats
print(f"{ratio * 100}% of fruit bats are male")
