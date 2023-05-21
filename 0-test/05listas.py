# Listas & Arrays =>
inventory = ["Iron Breastplate", "Healing Potion", "Leather Scraps"]
print(inventory)  # ['Iron Breastplate', 'Healing Potion', 'Leather Scraps']

# Acceder a elementos con su indice =>
print(inventory[1])  # Healing Potion

# Ejemplo =>
inventory = ["Healing Potion", "Leather Scraps",
             "Iron Helmet", "Bread", "Shortsword"]
item_index = 1
item = inventory[item_index]

# Longitud de un array =>
fruits = ["apple", "banana", "pear"]
length = len(fruits)
print(length)  # 3

# Ultima posicion de la lista =>
inventory = [
    "Potion",
    "Iron Breastplate",
    "Leather Scraps",
    "Iron Ore",
    "Light Leather",
    "Bread",
    "Shortsword",
    "Longsword",
    "Iron Mace",
]
last_index = len(inventory) - 1
print(last_index)

# Actualizar elementos de una lista =>
inventory = ["Leather", "Healing Potion", "Iron Ore"]
inventory[0] = "Leather Armor"
print(inventory)

# Ejemplo =>
inventory = ["Healing Potion", "Iron Ore", "Bread", "Shortsword"]
print(inventory)
inventory[1] = "Iron Bar"

# Agregar elementos a una lista python => .append
cards = []
cards.append("nvidia")
cards.append("amd")

# Ejemplos =>
player_ids = []
for i in range(0, 100):
    player_ids.append(i)
print(player_ids)

# Eliminar el ultimo elemento de una lista =>
vegetables = ["broccoli", "cabbage", "kale", "tomato"]
last_vegetable = vegetables.pop()

# Ejemplo =>
inventory = [
    "Healing Potion",
    "Iron Bar",
    "Kite Shield",
    "Shortsword",
    "Leather Scraps",
    "Tattered Cloth",
]
print(f"inventory: {inventory}")
for i in range(0, len(inventory)):
    item = inventory.pop()

# Encontrar elementos especificos for =>
items = [
    "Potion",
    "Leather Scraps",
    "Bread",
    "Iron Ore",
    "Light Leather",
    "Bread",
    "Shortsword",
    "Longsword",
    "Iron Mace",
    "Shortsword",
    "Shortsword",
]

potion_count = 0
bread_count = 0
shortsword_count = 0

for i in range(0, len(items)):
    print(items[i])
    if items[i] == "Potion":
        potion_count += 1
    elif items[i] == "Bread":
        bread_count += 1
    elif items[i] == "Shortsword":
        shortsword_count += 1

# Buscar un elemento en una lista =>
inventory = ["Potion", "Healing Potion", "Iron Breastplate", "Leather Scraps"]
found = False

for i in inventory:
    if i == "Leather Scrap":
        found == True

if found:
    print("Found the leather scraps!")
else:
    print("Couldn't find the leather scraps!")


# Comparar elementos "diferentes" en una lista =>
old_character_levels = [1, 42, 43, 53, 12, 3, 32, 34, 54, 32, 43]
new_character_levels = [1, 42, 41, 52, 12, 3, 32, 12, 54, 32, 43]
for i in range(0, len(old_character_levels)):
    if old_character_levels[i] != new_character_levels[i]:
        print("nashe")

# Operador Modulo en python =>
print(7 % 3)  # 1

# Pushear numeros impares a una lista =>
odd_numbers = []
for i in range(0, 300):
    if i % 2 == 1:
        odd_numbers.append(i)
print(odd_numbers)

# Dividir / Cortar -> listas
#         0  *1   2   *3   4   5
scores = [50, 70, 30, 20, 90, 10, 50]
print(scores[1:5:2])  # [70,20] -> index 1 && 3

# Toda una seccion de una lista
scores = [50, 70, 30, 20, 90, 10, 50]
print(scores[1:5])  # [70, 30, 20, 90]

# Desde hasta el final de una lista =>
scores = [50, 70, 30, 20, 90, 10, 50]
print(scores[4:])  # [90, 10, 50]


# Ejemplo =>
champions = [
    "Thrundar",
    "Morgate",
    "Gandolfo",
    "Thraine",
    "Norwad",
    "Gilforn",
]

print(champions[3:])
print(champions[:3])
for a, i in enumerate(champions):
    if a % 2 == 0:
        print(i)


# Concatenacion de listas / Arrays =>
all = [1, 2, 3] + [4, 5, 6]
print(all)  # [1, 2, 3, 4, 5, 6]

# Ejemplo =>
johns_favorites = ["sword", "shield"]
jacks_favorites = ["potion", "hat"]
breannas_favorites = ["feather", "lance"]
new = johns_favorites + jacks_favorites + breannas_favorites
print(new, len(new))

# verificar si un elemento pertenece a la lista => "CONTIENE"
fruits = ["apple", "orange", "banana"]
print("banana" in fruits)  # True

# Ejemplo =>
top_weapons = [
    "sword of justice",
    "sword of slashing",
    "stabby daggy",
    "great axe",
    "silver bow",
    "spellbook",
    "spiked knuckles",
]

print(f"sword of justice is a top weapon: {'sword of justice' in top_weapons}")
print(f"great axe is a top weapon: {'great axe ' in top_weapons}")
print(f"silver bow is a top weapon: {'silver bow' in top_weapons}")

# Eliminacion en listas => "del"
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
del nums[3]
print(nums)  # [1, 2, 3, 5, 6, 7, 8, 9]

# ELiminar rangos de elementos en una lista =>
del nums[1:3]
print(nums)  # [1, 5, 6, 7, 8, 9]

# Eliminar todos los elementos de la lista =>
del nums[:]
print(nums)  # []

# ELimina datos =>
strongholds = [
    "Rivendale",
    "The Morgoth Mountains",
    "The Lonely Island",
    "Mordia",
    "Mordane",
    "Gondolin",
]
del strongholds[0]
print(strongholds)
del strongholds[3:5]
print(strongholds)

# Tuplas =>
my_tuple = ("this is a tuple", 45, True)
print(my_tuple[0])  # this is a tuple
print(my_tuple[1])  # 45
print(my_tuple[2])  # True

# Tuplas dentro de listas =>
my_tuples = [
    ("this is the first tuple in the list", 45, True),
    ("this is the second tuple in the list", 21, False)
]
print(my_tuples[0])  # ('this is the first tuple in the list', 45, True)
print(my_tuples[1][1])  # 21
print(my_tuples[1][2])  # False

# Convertir array en tupla =>
heroes = [
    "Glorfindel",
    2093,
    True,
    "Gandalf",
    1054,
    False,
    "Gimli",
    389,
    False,
    "Aragorn",
    87,
    False,
]
hero_tuples = []
for i in range(0, len(heroes), 3):
    hero_name = heroes[i]
    hero_age = heroes[i+1]
    hero_is_elf = heroes[i+2]
    hero_tuples.append((hero_name, hero_age, hero_is_elf))
print(hero_tuples)

# Ejemplo
numbers = [
    0,
    99,
    2,
    33,
    61,
    44,
    9,
    10,
    12,
    240,
    35,
    9082,
    1234,
]
num_evens = 0
num_odds = 0

for i in numbers:
    print(i)
    if i % 2 == 0:
        num_evens += 1
    else:
        num_odds += 1


# Ejemplo =>
players = [
    "Harry",
    "Hermione",
    "Ron",
    "Ginny",
    "Fred",
    "Neville",
    "Draco",
    "Luna",
    "Cho",
    "Gregory",
    "Lee",
    "Michael",
    "Lavender",
    "Frank",
    "Anthony",
]
a = []
b = []
for i in range(0, len(players)):
    if i % 2 == 0:
        a.append(players[i])
    else:
        b.append(players[i])
print(a)
print(b)

# Ejemplo =>
answer_sheet = ["A", "A", "C", "D", "D", "B", "C"]
student_answers = ["A", "B", "C", "A", "D", "B", "C"]
a = []
z = 0
for i in range(0, len(answer_sheet)):
    if answer_sheet[i] == student_answers[i]:
        z += 1

p = z*100/len(answer_sheet)
print(p)
