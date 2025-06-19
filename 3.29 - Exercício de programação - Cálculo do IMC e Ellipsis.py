nome = 'Ricardo Estevão'
altura = 1.89
peso = 90.0
imc = peso / (altura * altura)
print(f'Meu nome é {nome} e tenho {altura}m de altura')
print(f'Peso de {peso}KG e meu IMC é {imc:.2f}')

# O que o código abaixo exibe?

nome = "Luiz"
idade = 23
formato = '{n} tem {i} anos'
print(formato.format(n=nome, i=idade))