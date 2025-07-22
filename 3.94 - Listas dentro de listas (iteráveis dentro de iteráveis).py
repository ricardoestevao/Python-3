"""
Lista dentro de lista e seus índices
"""

salas = [
        # 0       # 1 - Valor dentro do indice
    ['Ricardo', 'Nair'], # 0 - Indice 0 dentro da lista
        # 0     - Valor dentro do indice
    ['Lucas'], # 1 - Indice 1 dentro da lista
        # 0          # 1            #2      - Valor dentro do indice
    ['Elizebete', 'Anontonio', 'Rodrigo',], # 2 - Indice 2 dentro da lista
]

print(salas[0][0])
print([salas[2][0]])

print('-' * 120)

salas1 = [
        # 0       # 1 - Valor dentro do indice
    ['Ricardo', 'Nair'], # 0 - Indice 0 dentro da lista
        # 0     - Valor dentro do indice
    ['Lucas'], # 1 - Indice 1 dentro da lista
        # 0          # 1            #2      - Valor dentro do indice
    ['Elizebete', 'Anontonio', 'Rodrigo',(0, 10, 20, 30, 40)], # 2 - Indice 2 dentro da lista
]

print(salas1[2][3][2]) # 1°[2] busca o indice, 2°[3] busca o valor dentro do indice, 3°[2] busca o valor dentro da tupla, que está dentro do valor do indice. 

for sala in salas:
    print(f'A sala é {sala}')
    for aluno in sala:
        print(aluno)