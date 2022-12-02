# Generated by Django 4.1.1 on 2022-12-02 17:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0003_tracking'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cita',
            name='especialista',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app.especialista'),
        ),
        migrations.AlterField(
            model_name='cita',
            name='estado',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app.estado_cita'),
        ),
        migrations.AlterField(
            model_name='cita',
            name='lugar',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app.region'),
        ),
        migrations.AlterField(
            model_name='cita',
            name='usuario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='citas', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='comuna',
            name='region',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app.region'),
        ),
        migrations.AlterField(
            model_name='especialista',
            name='especialidad',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app.especialidad'),
        ),
        migrations.AlterField(
            model_name='especialista',
            name='region',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app.region'),
        ),
        migrations.AlterField(
            model_name='especialista',
            name='tipo_titulo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app.titulo'),
        ),
        migrations.AlterField(
            model_name='fichaatencion',
            name='especialista',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app.especialista'),
        ),
        migrations.AlterField(
            model_name='fichaatencion',
            name='paciente',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app.paciente'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='convenio',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app.convenio'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='fecha_nacimiento',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='prevision',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app.prevision'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='telefono',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='taller',
            name='especialista',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app.especialista'),
        ),
        migrations.AlterField(
            model_name='tutor',
            name='paciente',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app.paciente'),
        ),
    ]