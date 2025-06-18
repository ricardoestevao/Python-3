# conversão de tipos, coerção, tyoe convertion, typecasting, coercion - São praticamentes a mesma coisa, é o atode converter um tipo em outro. 
# tipo imutáveis e primitivos: str, iten, float, bool. 

# print(1 + 'b') # Não é possivel somar uma string com um número inteiro

print('1', type('1')) # Type de dados = Nesse cado o 1 está como uma string e não como um número inteiro. 
print(int('1'), type(int('1'))) # O int nesse código fez a conversão da string para um número inteiro. 
print(int('1') + 1) # Outra forma de conversão de string para número inteiro ou float. 
print(bool('')) # bool retorna True ou False, para True: É só ter um valor dentro da string e False é deixar sem nada, até sem espaço. 
print(str(11) + 'Ricardo') # Para conversão de um número intero para uma string, colocamos o str na frente do número a ser convertido. 