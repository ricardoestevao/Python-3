frase = 'O Python é uma linguagem de programação'\
    'multiparadigma' \
    'Python for criado por Guido Van Rossum.'


i = 0 
letras_contagem = {}  # dicionário para contar as letras 

while i < len(frase): # enquanto i for menor que o tamanho da frase
    letra_atual = frase[i] # pega a letra atual da frase
    if letra_atual == ' ': # se a letra atual for um espaço, pula para a próxima iteração
        i += 1 # incrementa i para passar para a próxima letra
        continue # pula o espaço em branco

    if letra_atual in letras_contagem: # se a letra já estiver no dicionário, incrementa a contagem
        letras_contagem[letra_atual] += 1 # incrementa a contagem da letra atual
    else: # se a letra não estiver no dicionário, adiciona com contagem 1
        letras_contagem[letra_atual] = 1 # adiciona a letra com contagem 1
    i += 1 # incrementa i para passar para a próxima letra

letras_mais_repetida = ''  # variável para armazenar a letra mais repetida
qtd_mais_repedita = 0  # variável para armazenar a quantidade da letra mais repetida

for letra, qtd in letras_contagem.items(): # itera sobre o dicionário de letras e suas contagens
    if qtd > qtd_mais_repedita: # se a quantidade da letra atual for maior que a quantidade mais repetida
        letras_mais_repetida = letra # atualiza a letra mais repetida
        qtd_mais_repedita = qtd # atualiza a quantidade mais repetida

print(f'A letra que mais apareceu foi {letras_mais_repetida} em {qtd_mais_repedita} vezes')
  