from csv import reader
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import re
from pickle import dump, load

class Gerenciador():
    def __init__(self):
        self.revisoes = []
        self.recomendacoes = []

        try:
            print("Tentando carregar revisões processadas...")
            self.carregar()
            print("As revisões processadas foram carregadas.")
        except:
            print("A tentativa falhou. Extraindo e processando revisões...")
            revisoes_positivas = self.extrair("revisoes_positivas.csv")
            revisoes_negativas = self.extrair("revisoes_negativas.csv")
            self.processar(revisoes_positivas)
            self.processar(revisoes_negativas)
            self.salvar()
            print("As revisões foram extraídas, processadas e salvas.")

    def carregar(self):
        with open("revisoes_processadas.pickle", "rb") as arquivo:
            self.revisoes, self.recomendacoes = load(arquivo)

    def salvar(self):
        with open("revisoes_processadas.pickle", "wb") as arquivo:
            dump([self.revisoes, self.recomendacoes], arquivo)

    def extrair(self, caminho):
        with open(caminho,encoding="utf8") as arquivo:
            dados_carregados = reader(arquivo, delimiter=";")
            return list(dados_carregados)

    def processar(self, revisoes):
        revisoes_processadas = list(map(lambda i: self.processador(i[1].lower()), revisoes))
        list(map(lambda i: self.inserir_revisao(i), revisoes_processadas))
        list(map(lambda i: self.inserir_recomendacao(i[0]), revisoes))

    def processador(self, revisao):
        lista_stopwords = stopwords.words("portuguese")
        stopwords_desconsideradas = ["não", "é", "mas"]
        list(map(lambda i: lista_stopwords.remove(i), stopwords_desconsideradas))

        resultado = revisao.replace("'", "")
        
        resultado = re.sub("\W", " ", str(resultado))
        resultado = re.sub("\s+[a-zA-Z]\s+", " ", resultado)
        
        resultado = list(map(lambda i: re.sub("[^A-Za-z]+", " ", i), [resultado]))
        resultado = list(map(lambda i: word_tokenize(i), resultado))
        resultado = list(map(lambda i: list(filter(lambda j: j not in lista_stopwords, i)), resultado))
        
        lemmatizer = WordNetLemmatizer()
        resultado = list(map(lambda i: list(map(lambda j: lemmatizer.lemmatize(j), i)), resultado))
        resultado = " ".join(resultado[0])
        
        return resultado

    def inserir_revisao(self, revisao):
        self.revisoes.append(revisao)

    def inserir_recomendacao(self, recomendacao):
        self.recomendacoes.append(recomendacao)