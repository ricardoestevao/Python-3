"""
Exercicio - Peça ao usuário para digitar seu nome e sua idade.
# Se o nome e idade forem digitados:
    Exiba: 
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espeços
        Seu nome tem {n} letras
        A primeira letra do seu nomeé {letra}
        A última letra do seu nomeé {letra}
Se nada for digitado em nome ou idade:
    Exiba " Desculpe, você deixou campos vazios


"""

nome = str(input('Digite o seu nome completo: '))
idade_input = input('Digite a sua idade: ')

if not nome or not idade_input:
    print('Desculpe, você deixou campos vazios')
else:
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')
    if ' ' in nome:
        print(f'Seu nome contém espaços')
    else:
        print(f'Seu nome não contém espaços')
    print(f'Seu nome tem {len(nome.replace(" ", ""))} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A ultima letra do seu nome é {nome[-1]}')