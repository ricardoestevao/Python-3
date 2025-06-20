"""
Interpolação básica de strings  = Interpolação, em programação, é o processo de inserir valores de variáveis dentro de uma string
s = string
d e i - int
f - float
x e X - Hexadecimal - (ABCDEF0123456789) o 'x' converter em hexadecimal minúsculo e X converte hexadecimal maiúsculo.
"""

nome = 'Ricardo'
altura = 1.89
variavel = '%s, tem %.2fm de altura' % (nome, altura)
print(variavel)

nome = 'Nair'
mensagem = 'Olá %s!' % nome
print(mensagem)

print('O hexadecimal de %d é %X' % (6, 7))

