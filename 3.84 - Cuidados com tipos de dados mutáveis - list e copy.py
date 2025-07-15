"""
Cuidados com dados mutáveis

= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória(mutável)

"""

nome = 'Ricardo'
noutra_variavel = nome
nome = 'Nair'
print(nome)
print(noutra_variavel)

lista_a = ['Ricardo', 'Nair'] # lista_b = lista_a.copy()  # Copia a lista, criando uma nova referência
lista_b = lista_a # lista_b = lista_a.copy()  # Copia a lista, criando uma nova referência

lista_a[0]= 'Qualquer coisa' # lista_b[0] = 'Qualquer coisa'  # Isso também alteraria a lista_b, pois ambas apontam para o mesmo objeto na memória
print(lista_b)
