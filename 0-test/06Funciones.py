# Funciones =>

# Funcion calcular area ->
def area_of_circle(r):
    return 3.14 * r * r


z = area_of_circle(5)
print(z)

# Funciones con multiples parametros =>


def subtract(a, b):
    return a - b


rta1 = subtract(10, 5)
print(rta1)  # 5


# Funcion calcula el daño
def calculate_damage(enemy_one_dmg, enemy_two_dmg, enemy_three_dmg):
    return enemy_one_dmg + enemy_two_dmg + enemy_three_dmg


print(f"You dealt {calculate_damage(2, 3, 4)} points of damage!")
print(f"You dealt {calculate_damage(-1, 4, 3)} points of damage!")
print(f"You dealt {calculate_damage(3, 2, 4)} points of damage!")
print(f"You dealt {calculate_damage(1, 4, 2)} points of damage!")


# Ejemplo =>
def get_max_health(modifier, level):
    return modifier * level


my_modifier = 5
my_level = 10
max_health = get_max_health(my_modifier, my_level)


# Ejemplo =>
player_level = 4


def calculate_health(modifier):
    return player_level * modifier


def calculate_primary_stats(armor_bonus, modifier):
    return armor_bonus + modifier + player_level


print(f"Character has {calculate_health(10)} max health.")
print(f"Character has {calculate_primary_stats(3, 8)} primary stats.")


# Funcion calcula "celcius" =>
def to_celsius(f):
    return 5/9 * (f-32)


def test(f):
    c = round(to_celsius(f), 2)
    print(f"{f} degrees fahrenheit is {c} degrees celsius")


test(100)
test(88)
test(104)
test(112)


#
def string_exists(string_to_check, string_array):
    if string_to_check in string_array:
        return True


def test(string_to_check, string_array):
    exists = string_exists(string_to_check, string_array)
    if exists:
        print(f"{string_to_check} exists in {string_array}")
    else:
        print(f"{string_to_check} does NOT exist in {string_array}")


test("Healing Potion", ["Iron Bar", "Leather Scraps", "Shortsword"])
test("Iron Helmet", ["Buckler", "Leather Armor Kit", "Iron Breastplate"])
test("Iron Ore", ["Healing Potion", "Iron Ore", "Cheese"])
test("Shortsword", ["Potion", "Iron Breastplate", "Shortsword"])


# Logica Booleana =>

# SINTAXIS "Y"
def is_dog(num_legs, weight):
    return num_legs == 4 and weight < 100


# SINTAXIS "O"
def is_car_cool(speed, is_electric):
    return speed > 200 or is_electric


# Ejemplo =>
def does_attack_hit(attack_roll, armor_class):
    return attack_roll != 1 and attack_roll >= armor_class


def test(attack_roll, armor_class):
    hits = does_attack_hit(attack_roll, armor_class)
    if hits:
        print(
            f"With a roll of {attack_roll} and armor class of {armor_class} the attack hits!"
        )
    else:
        print(
            f"With a roll of {attack_roll} and armor class of {armor_class} the attack does NOT hit!"
        )


test(17, 18)
test(20, 25)
test(1, 0)
test(16, 13)
test(25, 21)


# Convetir horas en segundos =>
def convert_hours_to_seconds(hours):
    return (hours * 60) * 60


def test(hours):
    secs = convert_hours_to_seconds(hours)
    print(f"{hours} hours is {secs} seconds")


test(10)
test(1)
test(2.5)
test(100)
test(33)


# Ejemplo =>
def get_first_item(items):
    if items == []:
        return "ERROR1"
    else:
        return items[0]


def test(items):
    first = get_first_item(items)
    print(f"First item in {items} is: {first}")


test([1, 2])
test(["Healing Potion"])
test(["Iron Ore", "Iron Bar", "Scimitar"])
test([])


# Ejemplo =>
def should_serve_customer(customer_age, on_break, time):
    return (time > 5 and time < 10) and on_break and customer_age > 21


def test(customer_age, on_break, time):
    should_serve = should_serve_customer(customer_age, on_break, time)
    print(
        f"age={customer_age}, on_break={on_break}, time={time}: should_serve={should_serve}"
    )


test(22, False, 8)
test(41, False, 1)
test(22, True, 8)
test(18, True, 3)
test(23, False, 9)
test(22, False, 11)
test(21, False, 9)
test(20, False, 9)

#
# NOS QUEDAMOS EN 17 =>
