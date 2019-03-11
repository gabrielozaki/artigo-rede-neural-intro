PESO_VIES = 0.1
w1 = 0.1
w2 = 0.1
passo = 0.2
treinamento = []

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
# treinamento = []
# treinamento.append(
#     {
#         "comprimento": 20,
#         "largura": 10,
#         "classe": 0
#     }
# )
# treinamento.append(
#     {
#         "comprimento": 80,
#         "largura": 60,
#         "classe": 1
#     }
# )
# treinamento.append(
#     {
#         "comprimento": -20,
#         "largura": 10,
#         "classe": 1
#     }
# )


soma = 0
finalizar = False
while True:
    if finalizar:
        break
    finalizar = True

    for i in treinamento:
        # print("Comprimento: " + str(i['comprimento']) + " | Largura: " + str(i['largura']) + "| w1:" + str(w1) + "| w2:" + str(w2))
        soma = ((i['comprimento']*w1)+(i['largura']*w2)) + (1*PESO_VIES)
        if soma > 0:
            Y = 1
        else:
            Y = 0
        erro = i['classe'] - Y

        if erro != 0:
            finalizar = False
        print("Comprimento: " + str(i['comprimento']) + " | Largura: " + str(i['largura']) + "| w1:" + str(w1) + "| w2:" + str(w2)
              + "| wv:" + str(PESO_VIES) + "| d:" + str(i['classe']) + "| net:" + str(soma) + "| Y:" + str(Y) + "| erro:" + str(erro))
        w1 += (passo*erro*i['comprimento'])
        w2 += (passo*erro*i['largura'])
        PESO_VIES += (passo*erro*1)
