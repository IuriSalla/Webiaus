import json
from django.shortcuts import render
from .AI import base
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.views.generic import View
from .utils import render_to_pdf
from django.template.loader import get_template

# Create your views here.

from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'home.html'

class AnaliseGraficoPageView(TemplateView):
    template_name = 'analise-grafico.html'

class UploadArquivoPageView(TemplateView):
    template_name = 'upload-arquivo.html'

def home(request):
    return render(request,'home.html',{})

def gerador_pdf(request, *args, **kwargs):
    pdf = render_to_pdf('grafico_pdf.html', {})
    return HttpResponse(pdf, content_type='application/pdf')

def upload(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['arquivo']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        url = fs.url(name)
        base_caminho = r"C:\Users\juans\OneDrive\Documentos\Webiaus\media'\'"
        base_caminho = base_caminho.replace("'",'')+name
        try: 
            contagem = base.analisador_sentimento(base_caminho)    
            return render(request,'grafico.html',{
                'contagemP': json.dumps([contagem[0]]),
                'contagemN': json.dumps([contagem[1]])
            })
        except:
            print("Tipo de arquivo incorreto!")
            return render(request,'home.html',{'Flag': json.dumps(True)})
        

