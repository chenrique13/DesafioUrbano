from django.urls import path
from . import views

urlpatterns = [
    path('', views.cadastrar, name='cadastrar'),
    path('consultar/', views.consultar, name='consultar'),
]
