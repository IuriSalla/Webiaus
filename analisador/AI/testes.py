import nltk
from nltk.corpus import stopwords
import pandas as pd

x = pd.read_excel(r"C:\Users\Juan Carlos\Documents\projeto_tg\frases.xlsx")
for i in x['texto']:
    print(i)


