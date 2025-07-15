"""
Introdução ao desempacotamento + tuples(tuplas)

"""

nome1, nome2, nome3 = ['Ricardo', 'Nair', 'Lucas']
print(nome1) # Apresenta apenas á variável solicitada

nome1, *resto = ['Ricardo', 'Nair', 'Lucas']
print(nome1, resto) # Apresenta o nome1 + as demais variáveis da lista como resto