# Variables =>

#
my_new_variable_two = 2
this_can_be_called_anything = 3
print(my_new_variable_two, this_can_be_called_anything)

#
player_health = 1000
print(player_health)

# Reasignacion de variables

acelearion1 = 5
acelearion1 = 10
print(acelearion1)

player_health = 900
print(player_health)

player_health = 800
print(player_health)

player_health = 700
print(player_health)

player_health = 600
print(player_health)

# Operadores matematicos basicos => + - * /

player_health = 1000
armor_multiplier = 2
armored_health = player_health * armor_multiplier
print(armored_health)

#
player_health = 6783424367754
poison_damage = -89743873
player_poison_health = player_health + poison_damage
print(player_poison_health)


# Tipos de datos => String, Numbers, float, bool
name_with_single_quotes = 'boot.dev'
name_with_double_quotes = "boot.dev"
x = 5
y = -5
x = 5.2
y = -5.2
hola = True
chau = False

# Variable vacias => None
vacia = None

# Las variables en python son de escritura dinamica =>
speed = 5
print(type(speed))  # <class 'int'>
speed = "five"
print(type(speed))  # <class 'str'>

# Concatenation de string =>
first_name = "Lane "
last_name = "Wagner"
full_name = first_name + last_name

# Variables multiples =>
sword_name, sword_damage, sword_length = "Excalibur", 10, 200
print(sword_name)
print(sword_damage)
print(sword_length)

# Promedio de equipos
game_one_score = 97
game_two_score = 91
game_three_score = 106
game_four_score = 105
game_five_score = 96
game_six_score = 93
game_seven_score = 104
average_score = (game_one_score+game_two_score+game_three_score +
                 game_four_score+game_five_score+game_six_score+game_seven_score)/7
print(round(average_score))


# Concatenacion de variables =>
part_one = "Roses are red, "
part_two = "violets are blue."
part_three = "Python is cool, "
part_four = "and so are you!"
line_one = part_one, part_two
line_two = part_three, part_four

#
# hola facundo
