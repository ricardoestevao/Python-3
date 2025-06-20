"""
Formatação básica de strings
s - string
d - int
f- float
<número de digitos>f
x ou X - Hexadecimal
(Caractere)(><^)(Quantidade)
> - Esquerda
< - Direita
^ - Centro
Sinal - + ou -
Ex: 0>-100, .1f
Conversion flags - !r !s !a
"""

variavell = 'Ricardo'
print(f'{variavell}')
print(f'{variavell: >20}') # 20 caracteres há esquerda
print(f'{variavell: <20}.') # 20 caracteres há direita
print(f'.{variavell: ^20}.') # 20 caracteres centralizado
print(f'{variavell:-^20}') # Logo após os dois pontos você pode colocar o caracteres desejavél, depois a centralização e por fim a quantidade. 
print(f'{100.654465465465:.1f}') # formatação :.1f com um número de casa decimal logo após o ponto
print(f'O Hexadecimal de 1500 é {1500:08X}')