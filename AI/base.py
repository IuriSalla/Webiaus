from gerenciador import Gerenciador
from vetorizador import CountVectorizer, TFIDFVectorizer
from classificador import NaiveBayes, SVM
from util import analisar_sentimento
import pandas as pd


gerenciador = Gerenciador()
revisoes = gerenciador.revisoes
recomendacoes = gerenciador.recomendacoes

vetorizador1 = CountVectorizer(revisoes)
vetorizador2 = CountVectorizer(revisoes,(1,4))

vetorizador3 = TFIDFVectorizer(revisoes)
vetorizador4 = TFIDFVectorizer(revisoes,(1,4))


classificador1 = NaiveBayes("naive_bayes_1_1_pt2.pickle",vetorizador1,recomendacoes)
classificador2 = NaiveBayes("naive_bayes_1_4_pt2.pickle",vetorizador2,recomendacoes)
classificador3 = SVM("svm_1_1_pt2.pickle",vetorizador3,recomendacoes)
classificador4 = SVM("svm_1_4_pt2.pickle",vetorizador4,recomendacoes)

print(classificador1.marcador())
print(classificador2.marcador())
print(classificador3.marcador())
print(classificador4.marcador()) #apresentou o melhor resultado

#C:\Users\Juan Carlos\Documents\projeto_tg\frases.xlsx
def analisador_sentimento(caminho):
    frases = pd.read_excel(r"caminho")
    for frase in frases['texto']:
        texto = frase
        print("----------------")
        #analisar_sentimento(classificador1,texto)
        #analisar_sentimento(classificador2,texto)
        #analisar_sentimento(classificador3,texto)
        analisar_sentimento(classificador4,texto)

