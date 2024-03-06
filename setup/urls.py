from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from faculdade import views


router = routers.DefaultRouter()
router.register(r'alunos', views.AlunoViewSet, basename='Alunos')
router.register(r'cursos', views.CursoViewSet, basename='Cursos')
router.register(r'matriculas', views.MatriculaViewSet, basename='matriculas')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('aluno/<int:pk>/matriculas/', views.ListaMatriculasPorAluno.as_view()),
    path('curso/<int:pk>/matriculas/', views.ListaAlunosPorCurso.as_view())
]
