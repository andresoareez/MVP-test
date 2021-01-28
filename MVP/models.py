from django.db import models
from django.contrib.auth.models import User


class DemandasDePecas(models.Model):

    STATUS = [
        ('Aberta', 'Aberta'),
        ('Finalizada', 'Finalizada'),
    ]

    descricao = models.TextField(max_length=300, verbose_name='Descrição da Peça')
    CEP = models.CharField(max_length=9, blank=False, null=False)
    logradouro = models.CharField(max_length=200, verbose_name='Endereço')
    bairro = models.CharField(max_length=100, verbose_name='Bairro')
    cidade = models.CharField(max_length=50, verbose_name='Cidade')
    numero = models.CharField(max_length=10, verbose_name='Nº')
    estado = models.CharField(max_length=2, verbose_name='Estado')
    email = models.CharField(max_length=100, verbose_name='Email', blank=False, null=False)
    telefone = models.CharField(max_length=10, verbose_name='Telefone')
    celular = models.CharField(max_length=11, verbose_name='Celular', blank=False, null=False)
    anunciante = models.OneToOneField(User, to_field='username', on_delete=models.CASCADE)
    status = models.CharField(max_length=10, verbose_name='Qual Status da Demanda?', choices=STATUS, default='Aberta')

    class Meta:
        verbose_name= 'Demanda de Peça'
        verbose_name_plural = 'Demanda de Peças'

    def __str__(self):
        return self.descricao

