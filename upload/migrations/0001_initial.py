# Generated by Django 4.0 on 2022-01-12 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Archivo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tarjeta', models.CharField(max_length=50)),
                ('tamaño', models.CharField(max_length=50)),
                ('fecha', models.DateTimeField(verbose_name='publicacion')),
            ],
        ),
    ]
