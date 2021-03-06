# Generated by Django 4.0.4 on 2022-06-29 02:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AsignacionCientifico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaDesde', models.DateField()),
                ('fechaHasta', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='CambioEstadoRT',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaHoraDesde', models.DateTimeField()),
                ('fechaHoraHasta', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='CambioEstadoTurno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaHoraDesde', models.DateTimeField()),
                ('fechaHoraHasta', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='CentroInvestigacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('fechaAlta', models.DateField()),
                ('fechaBaja', models.DateField()),
                ('asignacionCientifico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservaRT.asignacioncientifico')),
            ],
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('descripcion', models.CharField(max_length=100)),
                ('ambito', models.CharField(max_length=20)),
                ('esCancelable', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Modelo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservaRT.marca')),
            ],
        ),
        migrations.CreateModel(
            name='PersonalCientifico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('legajo', models.CharField(max_length=10)),
                ('nombre', models.CharField(max_length=20)),
                ('apellido', models.CharField(max_length=20)),
                ('numeroDocumento', models.CharField(max_length=8)),
                ('correoElectronicoPersonal', models.EmailField(max_length=254)),
                ('correoElectronicoInstitucional', models.EmailField(max_length=254)),
                ('telefonoCelular', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='RecursoTecnologico',
            fields=[
                ('numeroRT', models.IntegerField(primary_key=True, serialize=False)),
                ('fechaAlta', models.DateField()),
                ('fechaBaja', models.DateField()),
                ('imagenes', models.ImageField(upload_to='')),
                ('cambioEstadoRecursoTecnologico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservaRT.cambioestadort')),
                ('centroInvestigacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservaRT.centroinvestigacion')),
                ('modelo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservaRT.modelo')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=100)),
                ('clave', models.CharField(max_length=100)),
                ('habilitado', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Turno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaGeneracion', models.DateField()),
                ('diaSemana', models.CharField(max_length=10)),
                ('fechaHoraInicio', models.DateTimeField()),
                ('fechaHoraFin', models.DateTimeField()),
                ('cambioEstadoTurno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservaRT.cambioestadoturno')),
            ],
        ),
        migrations.CreateModel(
            name='TipoRecursoTecnologico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=100)),
                ('recursoTecnologico', models.ManyToManyField(to='reservaRT.recursotecnologico')),
            ],
        ),
        migrations.CreateModel(
            name='Sesion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservaRT.usuario')),
            ],
        ),
        migrations.AddField(
            model_name='recursotecnologico',
            name='tipoRecursoTecnologico',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservaRT.tiporecursotecnologico'),
        ),
        migrations.AddField(
            model_name='recursotecnologico',
            name='turno',
            field=models.ManyToManyField(to='reservaRT.turno'),
        ),
        migrations.AddField(
            model_name='centroinvestigacion',
            name='recursoTecnologico',
            field=models.ManyToManyField(to='reservaRT.recursotecnologico'),
        ),
        migrations.AddField(
            model_name='cambioestadoturno',
            name='estado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservaRT.estado'),
        ),
        migrations.AddField(
            model_name='asignacioncientifico',
            name='personalCientifico',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservaRT.personalcientifico'),
        ),
    ]
