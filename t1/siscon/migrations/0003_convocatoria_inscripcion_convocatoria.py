# Generated by Django 4.1.5 on 2023-06-08 14:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('siscon', '0002_remove_inscripcion_dni'),
    ]

    operations = [
        migrations.CreateModel(
            name='Convocatoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idarea', models.IntegerField()),
                ('nombre', models.CharField(max_length=30)),
                ('descripcion', models.CharField(max_length=200)),
                ('detalle', models.CharField(blank=True, max_length=1000)),
                ('estado', models.IntegerField()),
                ('inicio', models.DateField()),
                ('finalizacion', models.DateField()),
                ('link_insc', models.CharField(blank=True, max_length=200, null=True)),
                ('link_acuerdo', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='inscripcion',
            name='convocatoria',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='siscon.convocatoria'),
        ),
    ]