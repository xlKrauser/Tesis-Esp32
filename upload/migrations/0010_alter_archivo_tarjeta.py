# Generated by Django 4.0 on 2022-06-21 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0009_archivo_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='archivo',
            name='tarjeta',
            field=models.CharField(choices=[('T1', 'MODULO DOMOTICO'), ('T2', 'MODULO SENSOR TEMPERATURA'), ('T3', 'MODULO MOTOR ELECTRICO'), ('T4', 'MODULO INCUBADORA')], default='MODULO DOMOTICO', max_length=15),
        ),
    ]