# Generated by Django 4.0 on 2022-02-23 00:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('upload', '0016_archivo_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='archivo',
            name='usuario',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
        ),
    ]
