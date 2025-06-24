"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdareira

"""

contador = 0

while contador < 100:
    contador += 1

    if contador == 6:
        print('Não vou mostar o 6')
        continue    # O código irar rodar até chegar o 6 e pular o número caso a condição for verdadeira. 

    if contador >=10 and contador <= 27:
        print('Não vou mostrar o', contador)
        continue

    print(contador)

    if contador == 40:
        break

print('Acabou!')