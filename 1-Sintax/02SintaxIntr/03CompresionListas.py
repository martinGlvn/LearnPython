# List Comprehension

# Metodo sin list comprehension
a = []
for i in range(1, 10):
    a.append(i*2)

print(a)  # [2, 4, 6, 8, 10, 12, 14, 16, 18]

# Metodo con list comprehension
b = [i * 2 for i in range(1, 11)]
print(b)  # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]


# Metodo list comprehension con "condicional"
b = [i*2 for i in range(1, 11) if i % 2 == 0]
print(b)  # [4, 8, 12, 16, 20]
