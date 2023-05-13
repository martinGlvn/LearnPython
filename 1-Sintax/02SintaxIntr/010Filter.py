# Filter =>
n = [10, 24, 50, 23]
n_filters = list(filter(lambda x: x % 2 == 0, n))
print(n_filters)  # [10, 24, 50]


# Filter diccionarios =>
partidos = [
    {
        'local': 'bolivia',
        'visitante': 'paraguay',
        'goles_locales': 3,
        'goles_visitantes': 1,
        'resultado_local': 'Win'
    },
    {
        'local': 'Brasil',
        'visitante': 'Argentina',
        'goles_locales': 1,
        'goles_visitantes': 2,
        'resultado_local': 'Win'
    },
    {
        'local': 'italia',
        'visitante': 'chile',
        'goles_locales': 1,
        'goles_visitantes': 1,
        'resultado_local': 'Draw'
    },
]

futbol_list = list(
    filter(lambda item: item["resultado_local"] == 'Win', partidos))

print(futbol_list)
