from rest_framework import viewsets, generics
from rest_framework.permissions import AllowAny
from faculdade.models import Aluno, Curso, Matricula
from faculdade.serializer import AlunoSerializer, CursoSerializer, MatriculaSerializer, MatriculasPorAlunoSerializer, AlunosPorCursoSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class AlunoViewSet(viewsets.ModelViewSet):
    """
    Endpoint da API que permite adicionar e ler os Alunos
    """
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class CursoViewSet(viewsets.ModelViewSet):
    """
    Endpoint da API que permite adicionar e ler os Cursos
    """
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class MatriculaViewSet(viewsets.ModelViewSet):
    """
    Endpoint da API que permite adicionar e ler as Matriculas
    """
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class ListaMatriculasPorAluno(generics.ListAPIView):
    """
    Endpoint da API que permite vizualizar todas as matriculas que um aluno especifico possui 
    """
    def get_queryset(self):
        queryset = Matricula.objects.filter(aluno_id = self.kwargs['pk'])
        return queryset
    serializer_class = MatriculasPorAlunoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class ListaAlunosPorCurso(generics.ListAPIView):
    """
    Endpoint da API que permite vizualizar todos os alunos que um curso espoecifico possui
    """
    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id = self.kwargs['pk'])
        return queryset
    serializer_class = AlunosPorCursoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]