from rest_framework import serializers
from faculdade.models import Aluno, Curso, Matricula
from faculdade.validators import *



class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = ['id', 'nome', 'rg', 'cpf', 'data_nascimento']

    def validate(self, data):
        validacao_cpf = cpf_valido(data['cpf'])
        if not validacao_cpf['qnt_nums']:
            raise serializers.ValidationError({"cpf": "O cpf deve conter exatamente 11 digitos"})
        if not validacao_cpf['only_nums']:
            raise serializers.ValidationError({"cpf": "O cpf deve conter somente numeros"})
        if not rg_valido(data['rg']):
            raise serializers.ValidationError({"rg": "O rg deve conter exatamente 9 digitos"})
        return data


class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = ['id', 'codigo', 'descricao', 'nivel']


class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        fields = ['id', 'aluno', 'curso', 'periodo']


class MatriculasPorAlunoSerializer(serializers.ModelSerializer):
    curso = serializers.ReadOnlyField(source = 'curso.codigo')
    periodo = serializers.SerializerMethodField()
    class Meta:
        model = Matricula
        fields = ['curso','periodo']
    def get_periodo(self, obj):
        return obj.get_periodo_display()


class AlunosPorCursoSerializer(serializers.ModelSerializer):
    aluno_nome = serializers.ReadOnlyField(source = 'aluno.nome')
    class Meta:
        model = Matricula
        fields = ['aluno_nome']