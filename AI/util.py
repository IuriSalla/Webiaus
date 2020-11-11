def analisar_sentimento(classificador,texto):
    predicao = classificador.preditor_texto(texto)
    if (int(predicao[0])>0):
        res = "positivo"
    else: 
        res = "negativo"
    print("Esse texto é: %s"%res)