for i in range(10): # Se conter apenas um parâmetro em range é definido como o STOP.
    if i == 2: # Se o valor de i for igual a 2, o loop irá pular para a próxima iteração
        print('i é 2, pulando...') 
        continue # continue pula para a próxima iteração do loop

    if i == 8: # Se o valor de i for igual a 8, o loop irá parar completamente
        print('i é 8, seu else não executará')
        break # break interrompe o loop completamente

    for j in range(1, 3): # Se o loop interno for executado, ele irá iterar de 1 a 2
        print(i, j) # Exibe o valor de i e j

else: # O bloco else será executado se o loop for completo sem encontrar um break
    print('For completo com sucesso!')