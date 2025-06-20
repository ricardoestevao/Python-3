# Operador in e not in - 'in' significa estar entre e 'not in' significa não estar entre. 
# String são iteráveis - 

#  0 1 2 3 4 5 6 # Indice 
#  R I C A R D O 

nome = 'Ricardo'
print(nome[2])
print('i' in nome) # I está em Ricardo
print('R' not in nome) # R está em Ricardo
#______________________________________________________________________________________________________________________________

nome = input('Digite o seu nome: ') # Exemplo de uso do operador in
encontrar = input('Digite o que deseja encontrar: ').upper().lower() # upper()(transforma letras minusculas em maiúscula) e lower()(transforma letras maiuscula em minúsculas) para normalizar a busca

if encontrar in nome: # Se encontrar estiver em nome
    print(f'{encontrar} está em {nome}') # Se encontrar estiver em nome, printa que está em nome
else:
    print(f'{encontrar} não está em {nome}') # Se encontrar não estiver em nome, printa que não está em nome
#______________________________________________________________________________________________________________________________

variavel_a = 1 or 0
variavel_b = 0 or 1
print(variavel_a, variavel_a)