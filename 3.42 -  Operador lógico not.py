# Operador lógico "not" - Usado para inverter expressões
# not True = False
# not False = True

senha = input('Senha: ')

if senha == '123456':
    print('Entrou')
else:
    print('Senha incorreta.')
#________________________________________________________________________________________________________________________________
senha = input('Senha: ')

if senha != '123456':
    print('Senha incorreta')
else:
    print('Entrou!')

#_________________________________________________________________________________________________________________________________

senha = input('Senha: ')

if not senha:
    print('Você não digitou nada')
#_________________________________________________________________________________________________________________________________

print(not True) # Saída será False por que o 'not' fez a inversão da expressão.
print(not False) # Saída será True por que o 'not' fez inversão da expressão. 