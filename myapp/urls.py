from myapp import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import get_transcriptions

urlpatterns = [

    path('', views.index, name='index'),
    path('upload/', views.upload_and_process, name='upload_and_process'),
    path('get_transcriptions/', get_transcriptions, name='get_transcriptions'),
] 