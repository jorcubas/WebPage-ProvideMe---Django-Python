# Generated by Django 2.1.7 on 2019-05-02 18:10

import datetime
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
            name='agregadoFavoritosProveedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(default=datetime.date.today, verbose_name='Date')),
                ('texto', models.TextField(max_length=150)),
                ('approved', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='movimientos_pagina',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TipoMovimiento', models.CharField(max_length=45)),
                ('FechaMovimiento', models.DateField()),
                ('HoraMovimiento', models.TimeField()),
                ('UsuarioMovimiento', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='proveedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=45)),
                ('correo', models.CharField(max_length=45)),
                ('telefono', models.IntegerField()),
                ('calificacion', models.FloatField(default=0.0)),
            ],
        ),
        migrations.CreateModel(
            name='provincia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('promedio', models.IntegerField()),
                ('Proveedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='calif', to='proveedor.proveedor')),
                ('Usuario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='author', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ratings_prov',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=25)),
                ('calificacion', models.IntegerField()),
                ('comentario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratingComment', to='proveedor.Comentario')),
                ('rating', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proveedor.Rating')),
            ],
        ),
        migrations.CreateModel(
            name='reporteProveedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Proveedor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='proveedor.proveedor')),
                ('Usuario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='proveedor',
            name='provincia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proveedor.provincia'),
        ),
        migrations.AddField(
            model_name='comentario',
            name='Proveedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='proveedor.proveedor'),
        ),
        migrations.AddField(
            model_name='comentario',
            name='Usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='autor', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='agregadofavoritosproveedor',
            name='Proveedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='proveedor.proveedor'),
        ),
        migrations.AddField(
            model_name='agregadofavoritosproveedor',
            name='Usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
