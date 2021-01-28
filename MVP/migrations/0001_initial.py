# Generated by Django 3.1.5 on 2021-01-28 14:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DemandasDePecas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.TextField(max_length=300, verbose_name='Descrição da Peça')),
                ('CEP', models.CharField(max_length=9)),
                ('logradouro', models.CharField(max_length=200, verbose_name='Endereço')),
                ('bairro', models.CharField(max_length=100, verbose_name='Bairro')),
                ('cidade', models.CharField(max_length=50, verbose_name='Cidade')),
                ('numero', models.CharField(max_length=10, verbose_name='Nº')),
                ('estado', models.CharField(max_length=2, verbose_name='Estado')),
                ('telefone', models.CharField(max_length=10, verbose_name='Telefone')),
                ('celular', models.CharField(max_length=11, verbose_name='Celular')),
                ('status', models.BooleanField(default=False, verbose_name='Status de Finalização')),
                ('anunciante', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, to_field='username')),
                ('email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_email', to=settings.AUTH_USER_MODEL, unique=True)),
            ],
        ),
    ]
