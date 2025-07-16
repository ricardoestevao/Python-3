"""
Enumerate - enumera iteráveis (índices)

"""

lista = ['Ricardo', 'Nair', 'Lucas', 'Estevão']


for item in enumerate(lista): # Enumerate irar enumerar cada índice da lista criada
    print(item)

# Outra forma de trabalhar com o enumarete
print('-' * 120)
for item in enumerate(lista):
    indice, nome = item
    print(indice, nome)

print('-' * 120)
# Outra forma de trabalhar com o enumarete
for indice, nome in enumerate(lista):
    print(indice, nome)