
texto = 'Python' # string

novo_texto = ' ' # variável para armazenar o novo texto
for letra in texto: # percorre cada letra da string
    novo_texto += f'*{letra}' # adiciona a letra com um asterisco antes
    print(letra) # imprime a letra atual
print(novo_texto) # imprime o novo texto com asteriscos