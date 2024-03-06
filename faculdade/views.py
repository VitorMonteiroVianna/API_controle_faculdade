from django.http import JsonResponse
from rest_framework import viewsets
from faculdade.models import Aluno, Curso
from faculdade.serializer import AlunoSerializer, CursoSerializer


class AlunoViewSet(viewsets.ModelViewSet):
    """
    Endpoint da API que permite adicionar e ler os Alunos
    """
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer


class CursoViewSet(viewsets.ModelViewSet):
    """
    Endpoint da API que permite adicionar e ler os Cursos
    """
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer