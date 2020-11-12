from django.urls import path
from . import views


urlpatterns = [
   path('analise-grafico/',views.func_test, name = "analise-grafico"),
   path('upload/',views.upload, name = "upload")
]
