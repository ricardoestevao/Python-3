"""
Faça um programa que peça ao usuário para digitar um número inteiro, informe se este número é par ou ímpar. Caso o usuário não digite um número inteiro,
informe que não é um número inteiro.
"""

# entrada = input('Digite um número inteiro: ')

# try:
#     num = int(entrada)
#     if num % 2 == 0:
#         print('O número digitado é PAR')
#     else:
#         print('O número digitado é IMPAR')

# except:
#     print('O número digitado não é inteiro')

#________________________________________________________________________________________________________________

# Faça um programa que pergunta a hora ao usuário e baseando-se no horário descrito, exiba a saudação apropriada. EX.
# Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23. 

# horario = input('Que horas são? ')

# try:
#     hora = int(horario)
#     if 0 <= hora <= 11:
#         print('Bom dia!')
#     elif 12 <= hora <= 17:
#         print('Boa tarde!')
#     else:
#         print('Boa noite')

# except:
#     print('O valor digitado não é inteiro')


#______________________________________________________________________________________________________________________

# Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou menos escreva "Seu nome é curto"
# Se tiver entre 5 e 6 letras, escreva "Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande"

nome = input('Digite o seu primeiro Nome: ')

if len(nome) <= 4:
    print('Seu nome é curto!')

elif len(nome) <= 6:
    print('Seu nome é normal!')
else:
    print('Seu nome é muito grande!')