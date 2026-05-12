from django.urls import path
from . import views

urlpatterns = [
    path('tecnologias/', views.tecnologias_view, name='tecnologias'),
    path('projetos/', views.projetos_view, name='projetos'),
    path('competencias/', views.competencias_view, name='competencias'),
    path('conquistas/', views.conquistas_view, name='conquistas'),
    path('formacoes/', views.formacoes_view, name='formacoes'),
    path('licenciaturas/', views.licenciaturas_view, name='licenciaturas'),
    path('docentes/', views.docentes_view, name='docentes'),
    path('ucs/', views.ucs_view, name='ucs'),
    path('tfcs/', views.tfcs_view, name='tfcs'),
    path('', views.index_view, name='portfolio_index'),
]