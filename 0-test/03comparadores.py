# Operadores de comparacion =>
# < "menos que"
# > "mas grande que"
# <= "Menos que o igual a"
# >= "Mayor qué o igual a"
# == "igual a"
# != "no igual a"

#
is_bigger = 5 > 4
print(is_bigger)  # True


#
elon_height = 5
sara_height = 10
jill_height = 7
bob_height = 6
bob_taller_than_elon = bob_height > elon_height
sara_taller_than_elon = sara_height > elon_height
jill_taller_than_sara = jill_height > sara_height


#
hero_armor = 175
enemy_damage = 250
enough_armor = hero_armor >= enemy_damage  # False

# Incremento / Decremento -> Python
shield_armor = 4
shield_armor += 1  # 5
shield_armor += 2  # 7

shield_armor2 = 10
shield_armor2 -= 2  # 8
shield_armor2 -= 5  # 3

# Condicional IF =>

# Ejemplo
player_health = 0
if player_health == 0:
    print("dead!")  # evalua dead!
if player_health > 0:
    print("alive!")

# Ejemplo
number_of_swords = 500
number_of_soldiers = 1000
if number_of_swords < number_of_soldiers:
    print("We do not have enough swords for the army!")

# If Else =>
player_health = 4
if player_health == 0:
    print("dead")
elif player_health < 5:
    print("injured")
else:
    print("healthy")

# Ejemplo =>
current_player_name = "ash ketchum"
high_scoring_player_name = "ash ketchum"
if current_player_name == high_scoring_player_name:
    print("You are the highest scoring player!")
else:
    print("You are not the highest scoring player")

# Ejemplo =>
current_player_name = "brock harrison"
high_scoring_player_name = "ash ketchum"
lowest_scoring_player_name = "brock harrison"
if current_player_name == high_scoring_player_name:
    print("You are the highest scoring player!")
elif current_player_name == lowest_scoring_player_name:
    print("You are the lowest scoring player!")

# Ejemplo =>
time_purchased = 3
time_parked = 3
if time_parked >= time_purchased:
    print("You have been charged for overtime parking!")
else:
    print("Your time hasn't expired yet.")

# Ejemplo =>
player_power = 101
enemy_defense = 100
advantage, disadvantage, evenly_matched = False, False, False
if player_power > enemy_defense:
    advantage == True
elif player_power == enemy_defense:
    disadvantage == True
else:
    disadvantage == True

# Ejemplo =>
gallons_in_car = 8
miles_to_work = 105
miles_per_gallon = 22
gallons_needed = 176
if gallons_needed >= 176:
    print("You have enough gas to make it!")
else:
    print("You need more gas!")


# Ejemplo =>
total = 0
for i in range(0, 100):
    if not i % 2 == 0:
        total += i
        print(i)
    else:
        print("anashe")
print(total)

#
