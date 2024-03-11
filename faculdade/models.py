from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length = 50)
    rg = models.CharField(max_length = 9, unique = True)
    cpf = models.CharField(max_length = 11, unique = True)
    data_nascimento = models.DateField()

    def __str__(self):
        return self.nome


class Curso(models.Model):
    codigo = models.CharField(max_length = 10, unique = True)
    descricao = models.CharField(max_length = 256)
    NIVEL = (
        ('B', 'Basico'),
        ('I', 'Intermediario'),
        ('A', 'Avancado')
    )
    nivel = models.CharField(max_length = 1, choices = NIVEL, blank = False, default = 'B')

    def __str__(self):
        return self.codigo


class Matricula(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete = models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete = models.CASCADE)
    PERIODO = (
        ('I', 'Integral'),
        ('D', 'Diurno'),
        ('N', 'Noturno')
    )
    periodo = models.CharField(max_length = 1, choices = PERIODO, blank = False, default = 'I')