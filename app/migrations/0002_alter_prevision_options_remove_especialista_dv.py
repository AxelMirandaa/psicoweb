# Generated by Django 4.1.1 on 2022-12-06 20:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='prevision',
            options={'verbose_name': 'Previsión', 'verbose_name_plural': 'Previsiones'},
        ),
        migrations.RemoveField(
            model_name='especialista',
            name='dv',
        ),
    ]
