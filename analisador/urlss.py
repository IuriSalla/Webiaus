from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
   path('',views.home, name = "home"),
   path('upload/',views.upload, name = "upload"),
   path('pdf/',views.gerador_pdf, name = "gerador_pdf")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)