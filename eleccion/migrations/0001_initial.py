# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-01-31 23:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='circunscripcion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='mesa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='partidos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='resultado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resultado', models.IntegerField(default=0)),
                ('mesa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mesa', to='eleccion.mesa')),
                ('partido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='partido', to='eleccion.partidos')),
            ],
        ),
        migrations.AddField(
            model_name='mesa',
            name='partidos',
            field=models.ManyToManyField(to='eleccion.partidos'),
        ),
        migrations.AddField(
            model_name='circunscripcion',
            name='mesas',
            field=models.ManyToManyField(to='eleccion.mesa'),
        ),
    ]
