"""
CONSTANTE = "Variáveis" que não mudar # Normalmente as variáveis constante estão em letras maiúsculas o que significa que não pode atribiur novos valores a essa variável.
Muitas condições no mesmo if(ruim)
    <- Contagem de complexidade (ruim) - Quanto mais o código com espaçamento é mais complexo de ser lido
"""

velocidade = 60 # Velocidade atual do carro
local_carro = 100 # local em que o carro está na estrada

RADAR_1 = 60 # velocidade máxima do radar 1 
LOCAL_1 = 100 # local onde o radar 1 está
RADAR_RANGE = 1 # A distância onde o radar pega 

if velocidade > RADAR_1:
    print('Velocidade acima da máxima permitida!')

if local_carro >= (LOCAL_1 - RADAR_RANGE) and (LOCAL_1 + RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE) and velocidade > RADAR_1:
    print('CARRO MULTADO EM RADAR 1')