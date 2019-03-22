#Algumas variaveis fixas
PESO_VIES = 0.1
w1 = 0.1
w2 = 0.1
passo = 0.2
treinamento = []

#Criamos o treinamento
treinamento.append(
    {
        "comprimento": 21.2,
        "largura": 6.1,
        "classe": 1
    }
)

treinamento.append(
    {
        "comprimento": 20.9,
        "largura": 6.3,
        "classe": 1
    }
)

treinamento.append(
    {
        "comprimento": 12.1,
        "largura": 13,
        "classe": 0
    }
)

treinamento.append(
    {
        "comprimento": 11.9,
        "largura": 12.9,
        "classe": 0
    }
)

#Soma será o NET
soma = 0
#Variavel a ser analisada na condição de parada
finalizar = False

#Loop infinito
while True:
    #Condição de parada
    if finalizar:
        break
    
    #Preparação para a parada
    finalizar = True
    
    #Percorre todo o treinamento OBRIGATORIAMENTE
    for i in treinamento:
        #Calcula o NET
        soma = ((i['comprimento']*w1)+(i['largura']*w2)) + (1*PESO_VIES)
        
        #Aplica a função de transferencia
        if soma > 0:
            Y = 1
        else:
            Y = 0

        #Calcula o erro
        erro = i['classe'] - Y

        #Se acontecer um erro, evita a condição de parada
        if erro != 0:
            finalizar = False
        
        #Imprime as informaçoes
        print("Comprimento: " + str(i['comprimento']) + " | Largura: " + str(i['largura']) + "| w1:" + str(w1) + "| w2:" + str(w2)
              + "| wv:" + str(PESO_VIES) + "| d:" + str(i['classe']) + "| net:" + str(soma) + "| Y:" + str(Y) + "| erro:" + str(erro))
        
        #Atualiza os pesos(inclusive o de viés)
        w1 += (passo*erro*i['comprimento'])
        w2 += (passo*erro*i['largura'])
        #NOTA: o 1 não faz diferença, mas foi inserido para representar a entrada do peso de vies
        PESO_VIES += (passo*erro*1) 
