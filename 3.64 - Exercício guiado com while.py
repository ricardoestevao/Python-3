"""
Iterando strings com while

"""

nome = 'Ricardo Estevão' # Exemplo de iteração com while
# A ideia é iterar sobre cada letra da string e adicionar um asterisco antes de cada letra
nova_string = '' # String vazia para armazenar o resultado

i = 0 # Inicializando o índice i para 0
while i < len(nome): # Enquanto i for menor que o tamanho da string nome
    nova_string += f'*{nome[i]}' # Adiciona um asterisco antes da letra atual
    i += 1 # Incrementa o índice i para passar para a próxima letra

print(nova_string) # Resultado: *R*i*c*a*r*d*o* *E*s*t*e*v*ã*o

