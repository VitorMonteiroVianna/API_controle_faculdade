from django.contrib import admin
from faculdade.models import Aluno, Curso


class Alunos(admin.ModelAdmin):
    list_display = ('id', 'nome', 'rg', 'cpf', 'data_nascimento')
    list_display_links = ('id', 'nome')
    search_fields = ('id', 'nome', 'rg', 'cpf')
    list_per_page = 30

admin.site.register(Aluno, Alunos)


class Cursos(admin.ModelAdmin):
    list_display = ('codigo', 'descricao', 'nivel')
    list_display_links = ('codigo', 'descricao')
    search_fields = ('codigo',)
    list_per_page = 30

admin.site.register(Curso, Cursos)