#Script simples que gera nomes e documentos validos e insere no banco, para poder trabalhar com ppaginação e etc


import os, django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()

from faker import Faker
from validate_docbr import CPF
import random
from faculdade.models import Aluno

def criando_pessoas(quantidade_de_pessoas):
    fake = Faker('pt_BR')
    Faker.seed(10)
    for _ in range(quantidade_de_pessoas):
        cpf = CPF()
        nome = fake.name()
        data = fake.date_object().strftime('%Y-%m-%d')
        cpf = cpf.generate()
        rg = "{}{}{}{}".format(random.randrange(10, 99),random.randrange(100, 999),random.randrange(100, 999),random.randrange(0, 9) ) 


        
        p = Aluno(nome = nome, cpf = cpf, rg = rg, data_nascimento = data)
        p.save()

# criando_pessoas(50)