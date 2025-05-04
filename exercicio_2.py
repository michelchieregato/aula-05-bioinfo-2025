"""
#### Exercício 2 - Variantes Raras

Dado uma lista de dicionários, com ids de variantes e sua frequencia na população,
imprima apenas o nome das variantes com frequecia menor que 1% (0.01).

Exemplo:

Entrada:

variantes = {
    {"id": "rs123", "frequencia": 0.008},
    {"id": "rs456", "frequencia": 0.015},
    {"id": "rs789", "frequencia": 0.007},
}

Saída:

As variantes raras são:
rs123
rs789
"""

# Variantes fornecidas
variantes = [
    {"id": "rs789", "frequencia": 0.07},
    {"id": "rs101112", "frequencia": 0.03},
    {"id": "rs131415", "frequencia": 0.0005},
    {"id": "rs161718", "frequencia": 0.05},
    {"id": "rs192021", "frequencia": 0.09},
    {"id": "rs222324", "frequencia": 0.012},
    {"id": "rs252627", "frequencia": 0.0001},
    {"id": "rs282930", "frequencia": 0.06},
]
