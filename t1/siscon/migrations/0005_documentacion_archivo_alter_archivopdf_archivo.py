# Generated by Django 4.1.5 on 2023-06-15 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siscon', '0004_tipodoc_alter_inscripcion_persona_legajo_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='documentacion',
            name='archivo',
            field=models.FileField(default=0, upload_to='documentacion/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='archivopdf',
            name='archivo',
            field=models.FileField(upload_to='documentacion/'),
        ),
    ]
