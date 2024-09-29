# Generated by Django 5.1.1 on 2024-09-29 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faculdade', '0002_matricula'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='cpf',
            field=models.CharField(max_length=11, unique=True),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='rg',
            field=models.CharField(max_length=9, unique=True),
        ),
        migrations.AlterField(
            model_name='curso',
            name='codigo',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]
