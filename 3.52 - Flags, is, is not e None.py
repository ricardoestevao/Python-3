""""
Flag (Bandeira) - Marcar um Loca
none = não valor
is e is not = é ou não é (tipo, valor, identidade)
id = Identidade

"""
condicao = False # Variável de controle para saber se passou pelo if
passou_no_if = None # Inicializa a variável como None


if condicao: # Se a condição for verdadeira, executa o bloco
    passou_no_if = True # Marca que passou pelo if
    print('Faça algo') 
else: # Se a condição for falsa, executa o bloco alternativo
    print('Não faça algo') 

if passou_no_if is None: # Verifica se passou_no_if é None
    print('Não passou no if') 
else: # Se passou_no_if não é None, significa que passou pelo if
    print('Passou no if')