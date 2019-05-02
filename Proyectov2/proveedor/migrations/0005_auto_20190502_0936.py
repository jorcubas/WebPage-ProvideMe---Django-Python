# Generated by Django 2.1.7 on 2019-05-02 15:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('proveedor', '0004_movimientos_pagina'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='Usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='author', to=settings.AUTH_USER_MODEL),
        ),
    ]