from django.urls import path
from AppCoder.views import *

urlpatterns = [
    path('', inicio, name='inicio'),
    path('cursos/', curso, name='curso'),
    path('profesores/', profesores, name='profesores'),
    path('entregables/', entregables, name='entregables'),
    path('cursoFormulario/', cursoFormulario, name='cursoFormulario'),
    path('buscarcamada/', busquedaCamada, name='buscarcamada'),
    path('resultados/', resultados, name='resultadosbusqueda')

]