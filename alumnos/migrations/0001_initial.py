# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-06 14:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DatosPersonales',
            fields=[
                ('num_count', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=20)),
                ('sexo', models.CharField(max_length=1)),
                ('edad', models.IntegerField()),
                ('fechanacimiento', models.DateField()),
                ('telefono', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('domicilio', models.TextField()),
            ],
        ),
    ]
