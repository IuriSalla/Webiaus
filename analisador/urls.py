from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [path('', views.HomePageView.as_view(), name='home')]
urlpatterns = [path('', views.AnalisePageView.as_view(), name='analise-grafico')]
urlpatterns = [path('', views.UploadArquivoPageView.as_view(), name='upload-arquivo')]