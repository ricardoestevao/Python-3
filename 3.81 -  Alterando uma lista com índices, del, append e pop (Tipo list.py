"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: append, insert, pop, del, clear, extend, +

    append- Adiona um item ao final
    insert - adicona um item no indice escolhido
    pop - remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista

"""

lista = [10, 20, 30, 40]
lista[2] = 2000 # alterando número existente na lista
del lista[0] # deletei o indice 0 da lista
lista.append(3) # adicionei o número 3 no final da lista
lista.pop() # Irar remover o ultimo valor da lista
print(lista)

lista1 = ['RICARDO']
lista1.insert(0, 'W') # Adionei no indice 0 o valor 'W'
print(lista1)