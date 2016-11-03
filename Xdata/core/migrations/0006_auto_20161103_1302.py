# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-03 13:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20161103_0903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoa',
            name='cor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Cor'),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='sexo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Sexo'),
        ),
    ]