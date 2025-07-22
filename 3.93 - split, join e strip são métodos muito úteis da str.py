"""
split e join com list e str
split - Divide um String 
join - Une uma string
"""

frase = 'Ricardo Santos Estevão da Silva'
lista_palavras = frase.split()
print(lista_palavras)

frase_unidas = ''.join(frase)
print(frase_unidas)

frase_unidas = '$'.join(frase)
print(frase_unidas)