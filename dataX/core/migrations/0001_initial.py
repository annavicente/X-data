# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-28 01:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_matricula', models.DateField()),
                ('data_conclusao', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Cor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_nascimento', models.DateField()),
                ('data_conclusao_ensino_medio', models.DateField()),
                ('CEP', models.CharField(max_length=15)),
                ('cor', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.Cor')),
                ('matriculas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Aluno')),
            ],
        ),
        migrations.CreateModel(
            name='Sexo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sexo', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='pessoa',
            name='sexo',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.Sexo'),
        ),
    ]
