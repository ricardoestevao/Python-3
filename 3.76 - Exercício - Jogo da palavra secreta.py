"""
Faça um jogo para o usuário adivinhar qual a palavra secreta. Você vai propor uma palavra secreta qualquer e vai dar a possibilidade para o usuário digitar apenas uma letra.
Qual o usuário digitar uma letra, você vai conferir se a letra digitada está na palavra secreta.

    Se a letra digitada estiver na palavra secreta; exiba a letra;
    Se a letra digitada não estiver na palavra secreta; exiba *.

Faça a contagem de tentativas do seu usuário. 

"""

letra_secreta = 'R'
palavra_secreta = 'RICARDO'
tentavias = 0

while True:

    palavra = str(input('Qual a letra correta para o nome ao lado? "#ICARDO"  ')).upper()[0]
    tentavias += 1
    if palavra == letra_secreta:
        print(f'Você acertou a letra "{palavra}" e a palavra correta é {palavra_secreta}')
        print(f'Números de tentativas até o acerto: {tentavias} vezes')
        break

    else:
        print('Você digitou a letra errada *, tente novamente!')
    