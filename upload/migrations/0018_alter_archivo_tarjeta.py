# Generated by Django 4.0 on 2022-07-07 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0017_alter_archivo_tarjeta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='archivo',
            name='tarjeta',
            field=models.CharField(choices=[('T1', 'MODULO DOMOTICO'), ('T2', 'MODULO SENSOR TEMPERATURA'), ('T3', 'MODULO MOTOR ELECTRICO'), ('T4', 'MODULO INCUBADORA')], default=None, max_length=15),
        ),
    ]
