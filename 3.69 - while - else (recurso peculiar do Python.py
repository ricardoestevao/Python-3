"""
While / else

"""
string = 'Valor qualquer' # O laço while executa enquanto a condição for verdadeira

i = 0 # Variável de controle

while i < len(string): # Enquanto i for menor que o tamanho da string
    letra = string[i] # Acessa a letra na posição i da string

    print(letra) # Imprime a letra atual
    i += 1 # Incrementa i para passar para a próxima letra

else: # O bloco else é executado quando o laço while termina normalmente (sem break)
    print('O else foi executado') 

print('PRINT FORA DO WHILE') # Este print é executado após o laço while e o bloco else
print('_' * 130)

string = 'Valorqualquer' # String sem espaço

i = 0 # Variável de controle

while i < len(string): # Enquanto i for menor que o tamanho da string
    letra = string[i] # Acessa a letra na posição i da string
    
    print(letra) # Imprime a letra atual
    i += 1 # Incrementa i para passar para a próxima letra

else: # O bloco else é executado quando o laço while termina normalmente (sem break)
    print(f'Não encontrei espaço dentro de {string}') # Este print é executado após o laço while e o bloco else