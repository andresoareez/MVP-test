# Generated by Django 3.1.5 on 2021-01-28 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MVP', '0002_auto_20210128_1601'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='demandasdepecas',
            options={'verbose_name': 'Demanda de Peça', 'verbose_name_plural': 'Demanda de Peças'},
        ),
        migrations.AlterField(
            model_name='demandasdepecas',
            name='email',
            field=models.CharField(max_length=100, verbose_name='Email'),
        ),
    ]
