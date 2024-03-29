from django.urls import path
from app_cad_usuarios import views

urlpatterns = [
    # rota, view responsável e nome de referência
    
    # Página principal
    path('',views.home, name='home'),
    # Rota para adicionar/editar usuários 
    path('usuarios/',views.usuarios, name='usuarios'),
    
    path('listagem_usuarios/', views.usuarios,name='listagem_usuarios')
]
