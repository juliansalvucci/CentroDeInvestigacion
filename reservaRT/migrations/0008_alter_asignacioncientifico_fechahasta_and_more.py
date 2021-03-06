# Generated by Django 4.0.4 on 2022-06-30 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservaRT', '0007_alter_centroinvestigacion_asignacioncientifico_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asignacioncientifico',
            name='fechaHasta',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='personalcientifico',
            name='correoElectronicoInstitucional',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='personalcientifico',
            name='correoElectronicoPersonal',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='personalcientifico',
            name='numeroDocumento',
            field=models.CharField(blank=True, max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='personalcientifico',
            name='telefonoCelular',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
