"""
Introdução ao Try/Except

Try = Tentar executar código
Except = Ocorreu algum erro ao tentar executar

"""

numero_str = input('Vou dobrar o número que você digitar: ') # Exemplo de uso do try/except para capturar erros

try: 
    numero_float= float(numero_str) # Tenta converter a string para float
    print('FLOAT', numero_str) # Se a conversão falhar, o código dentro do except será executado
    print(f'O dobro de {numero_str} é {numero_float * 2}') # Se a conversão for bem-sucedida, o código continuará normalmente

except:
    print('Isso não é um número') # Se ocorrer um erro na conversão, a mensagem de erro será exibida