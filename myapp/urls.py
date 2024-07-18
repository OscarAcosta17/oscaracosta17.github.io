from myapp import views
from django.urls import path


urlpatterns = [

    path('', views.index, name='index'),
    path('upload/', views.upload_and_process, name='upload_and_process'),
]