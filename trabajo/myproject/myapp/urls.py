# myapp/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('mi-vista/', views.mi_vista, name='mi_vista'),
    # Define más URLs según las vistas que tengas
]
