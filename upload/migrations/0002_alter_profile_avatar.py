# Generated by Django 4.0 on 2022-03-28 01:07

from django.db import migrations, models
import upload.models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to=upload.models.user_directory_path_profile),
        ),
    ]