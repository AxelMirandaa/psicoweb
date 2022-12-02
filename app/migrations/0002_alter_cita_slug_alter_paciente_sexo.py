# Generated by Django 4.1.1 on 2022-12-02 15:16

import django.core.validators
from django.db import migrations, models
import re


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cita',
            name='slug',
            field=models.SlugField(unique=True, validators=[django.core.validators.RegexValidator(re.compile('^[-a-zA-Z0-9_]+\\Z'), 'Enter a valid “slug” consisting of letters, numbers, underscores or hyphens.', 'invalid')]),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='sexo',
            field=models.IntegerField(choices=[[0, 'Femenino'], [1, 'Masculino'], [2, 'No especificado']], null=True),
        ),
    ]
