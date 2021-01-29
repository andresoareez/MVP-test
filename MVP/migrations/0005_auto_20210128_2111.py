# Generated by Django 3.1.5 on 2021-01-28 21:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('MVP', '0004_auto_20210128_1624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='demandasdepecas',
            name='anunciante',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, to_field='username'),
        ),
    ]