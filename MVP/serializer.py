from rest_framework import serializers
from .models import DemandasDePecas
from .validadores import *


class DemandaDePecasSerializer(serializers.ModelSerializer):
    class Meta:
        model = DemandasDePecas
        fields = '__all__'

    def validate(self, dados):
        if not ValidaCep(dados['CEP']):
            raise serializers.ValidationError('O CEP não é Válido')
        if not ValidaTelefone(dados['telefone']):
            raise serializers.ValidationError('O Telefone não é Válido')
        if not ValidaCelular(dados['celular']):
            raise serializers.ValidationError('O celular não é Válido')
        return dados
