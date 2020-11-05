from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('analise-grafico/', views.AnaliseGraficoPageView.as_view(), name='analise-grafico'),
    path('upload-arquivo/', views.UploadArquivoPageView.as_view(), name="upload-arquivo")
]
