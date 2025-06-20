"""
Fatiamento de Strigns
012345678910
Ricardo Sant
-10987654321
Fatiamente [i:f:p] = 'i' (indice), 'f' (fatiamento), 'p' (passo) [::]
Obs: A função len retorn a qtd de caracteres da str
"""

variavel = 'Ricardo Santos Estevão da Silva'
print(variavel[4:12]) # O segundo digito do fatiamento deverá considerar +1 para ser selecionado Ex: rdo Sant - indice do 4 ao 11 
print(variavel[1:]) # Selecionei o indice 1 e não declarei o valor para o fatiamento 
print(len(variavel)) # 'len' conta quantidade de indice na variável
print(variavel[0:31:2]) # Indice '0', fatiamento até o indice 31, pulando de 2 em 2 indice