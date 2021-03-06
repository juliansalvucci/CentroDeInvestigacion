# Generated by Django 4.0.4 on 2022-06-29 22:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reservaRT', '0004_alter_personalcientifico_apellido_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recursotecnologico',
            name='cambioEstadoRecursoTecnologico',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='reservaRT.cambioestadort'),
        ),
        migrations.AlterField(
            model_name='recursotecnologico',
            name='centroInvestigacion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='reservaRT.centroinvestigacion'),
        ),
        migrations.AlterField(
            model_name='recursotecnologico',
            name='imagenes',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='recursotecnologico',
            name='modelo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='reservaRT.modelo'),
        ),
        migrations.AlterField(
            model_name='recursotecnologico',
            name='tipoRecursoTecnologico',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='reservaRT.tiporecursotecnologico'),
        ),
        migrations.AlterField(
            model_name='recursotecnologico',
            name='turno',
            field=models.ManyToManyField(blank=True, null=True, to='reservaRT.turno'),
        ),
    ]
