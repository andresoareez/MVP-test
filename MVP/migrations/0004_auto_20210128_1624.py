# Generated by Django 3.1.5 on 2021-01-28 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MVP', '0003_auto_20210128_1610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='demandasdepecas',
            name='status',
            field=models.CharField(choices=[('Aberta', 'Aberta'), ('Finalizada', 'Finalizada')], default='Aberta', max_length=10, verbose_name='Qual Status da Demanda?'),
        ),
    ]
