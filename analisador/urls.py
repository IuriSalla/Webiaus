from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
    path('upload-arquivo/', views.UploadArquivoPageView.as_view(), name="upload-arquivo"),
]
