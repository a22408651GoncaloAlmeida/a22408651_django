from django.urls import path
from . import views

urlpatterns = [
    path('', views.artigos_view, name='artigos'),
    path('<int:pk>/', views.artigo_detalhe, name='artigo_detalhe'),
    path('<int:pk>/like/', views.artigo_like, name='artigo_like'),
    path('criar/', views.artigo_criar, name='artigo_criar'),
    path('<int:pk>/editar/', views.artigo_editar, name='artigo_editar'),
    path('<int:pk>/apagar/', views.artigo_apagar, name='artigo_apagar'),
]