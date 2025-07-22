"""
Imprecisão de ponto flutuante

"""

numero_1 = 0.1
numero_2 = 0.7
numero_3 = numero_1 + numero_2
print(numero_3)
print(f'{numero_3:.2f}') # Normalmente usáriamos e o formatação do f-strings para corrigir
print(round(numero_3, 2)) # A função round é bem similar ao caso do f-string, porém essa função se mantem o type float ao invés de string como é o código acima.