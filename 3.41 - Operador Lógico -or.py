# Operadores lógicos and (e) or (ou) not(não)
# or - Qualquer condição verdadeira avalia toda a expressão como verdadeira. 
# são considerados falsy(que você já viu) 0 0.0 '' False
# Também existe o tipo None que é usado para representar um não valor. 

# entrada = input('[E]ntrar [S]air: ')
# senha_digitada = input('Senha: ')

# senha_permitida = '123456'

# if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida: # Foi colocado parenteses no or para ser executado primeiro
#     print('Entrar')
# else:
#     print('Sair')

#Avaliação de curto circuito
print(True or False) # Saida é True - Para o 'or' qualquer saida verdadeira dentro da condição. 
