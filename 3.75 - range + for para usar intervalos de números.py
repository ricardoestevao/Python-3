"""
For + Range
- Usar range para iterar sobre intervalos de números
range -> range(start, stop, step)

"""

numeros = range(10) # Se conter apenas um parâmetro em range é definido como o STOP. 
print(numeros)

print('_' * 130)

for n in range(5, 11): # Se for definido 2 parâmetros em range o primeiro é Start e a segunda Stop. Ultimo indice são é incluido
    print(n)

print('_' * 130)

for n in range(0, 21, 2): # Se for definido 3 parâmetros em range o primeiro é Start, o segundo Stop, e o terceiro o intervalo. Ultimo indice são é incluido
    print(n)