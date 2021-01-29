from django.contrib import admin
from .models import DemandasDePecas
from import_export.admin import ImportExportModelAdmin


class DemandaDePeca(ImportExportModelAdmin):
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
        'statusdemanda',
    ]
    list_display_links = [
        'descricao',
    ]
    list_filter = [
        'statusdemanda',
        'anunciante',
    ]
    search_fields = [
        'anunciante',
        'statusdemanda',
        'estado',
        'cidade',

    ]
    list_per_page = 50


admin.site.register(DemandasDePecas, DemandaDePeca)