"""
for in com listas

"""

lista = ['Ricardo', 'Nair', 'João', 'Maria'] # lista = ['Ricardo', 'Nair', 'João', 'Maria', 'Drogaria'] # Adicionando um novo item à lista
lista.append('Drogaria') # lista.append('Drogaria')  # Adicionando um novo item à lista

indices = range(len(lista)) # indices = range(0, len(lista))  # Cria um objeto range que representa os índices da lista



for indice in indices:  # for indice in range(len(lista)):  # Itera sobre os índices da lista
    print(indice, lista[indice], type(lista[indice])) # for indice in range(0, len(lista)):  # Itera sobre os índices da lista