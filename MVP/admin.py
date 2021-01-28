from django.contrib import admin
from .models import DemandasDePecas


class DemandaDePeca(admin.ModelAdmin):
    list_display = [
        'descricao',
        'CEP',
        'logradouro',
        'bairro',
        'cidade',
        'numero',
        'estado',
        'email',
        'telefone',
        'anunciante',
        'status',
    ]
    list_display_links = [
        'descricao',
    ]
    list_filter = [
        'status'
    ]
    list_editable = [
        'status'
    ]
    search_fields = [
        'anunciante',
        'status',
        'estado',
        'cidade',

    ]
    list_per_page = 50


admin.site.register(DemandasDePecas, DemandaDePeca)