# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-07-10 20:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_pessoa', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='cor',
            table='cor',
        ),
        migrations.AlterModelTable(
            name='forma_ingresso',
            table='forma_ingresso',
        ),
        migrations.AlterModelTable(
            name='pessoa',
            table='pessoa',
        ),
        migrations.AlterModelTable(
            name='profissao',
            table='profissao',
        ),
        migrations.AlterModelTable(
            name='renda_familiar',
            table='renda_familiar',
        ),
        migrations.AlterModelTable(
            name='reside',
            table='reside',
        ),
        migrations.AlterModelTable(
            name='responsavel',
            table='responsavel',
        ),
        migrations.AlterModelTable(
            name='sexo',
            table='sexo',
        ),
        migrations.AlterModelTable(
            name='tipo_escola_origem',
            table='tipo_escola_origem',
        ),
    ]