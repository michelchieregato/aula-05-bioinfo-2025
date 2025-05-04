"""
#### Exercício 1 - Buscando Informações de Genes

Você tem um dicionário onde:

A chave é o nome do gene.

O valor é o tamanho do gene (em pares de base).

Tarefa:

Peça para o usuário digitar o nome de um gene.

Depois, procure no dicionário:

Se o gene existir, imprima: "O tamanho do gene [NOME] é [TAMANHO] pb."

Se não existir, imprima: "Gene não encontrado."

------------

Exemplo:

Entrada:

Digite o nome do gene: BRCA1

Saída:

O tamanho do gene BRCA1 é [TAMANHO] pb."

------------

Exemplo:

Entrada:

Digite o nome do gene: BRCA3

Saída:

Gene não encontrado.
"""

genes = {
    "BRCA1": 81188,
    "TP53": 19054,
    "EGFR": 192612,
    "APOE": 3597,
    "CFTR": 250000,
    "HBB": 1606,
    "F8": 186000,
    "DMD": 2400000,
    "HTT": 169451,
    "FMR1": 38000,
}

# Criar seu código a partir daqui