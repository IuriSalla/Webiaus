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

def func_test(request):
    if request.method == 'POST':
        print("Foioooo")
    #essa função vai receber o arquivo/caminho e vai fazer a chamada da IA, depois do processamento
    #ela vai enviar para a 'analise-grafico.html' dois resultados , o número de frases positivas e negativas
    #os valores podem ser enviados em forma de vetor
    return render(request,'analise-grafico.html',{})

def upload(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['arquivo']
        print(uploaded_file.name)
        print(uploaded_file.size)   
    return render(request,'home.html')

