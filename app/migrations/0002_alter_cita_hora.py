# Generated by Django 4.0.4 on 2022-10-20 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cita',
            name='hora',
            field=models.IntegerField(null=True),
        ),
    ]
