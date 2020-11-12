from django.shortcuts import render
#from .AI import base
# Create your views here.

from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'home.html'

class AnaliseGraficoPageView(TemplateView):
    template_name = 'analise-grafico.html'

class UploadArquivoPageView(TemplateView):
    template_name = 'upload-arquivo.html'

#def func_test(request):
#    a = r"C:\Users\Juan Carlos\Documents\Webiaus\analisador\AI\frases.xlsx"
#    respostas = base.analisador_sentimento(a)
#    print(respostas)
#    return render(request,'analise-grafico.html')

