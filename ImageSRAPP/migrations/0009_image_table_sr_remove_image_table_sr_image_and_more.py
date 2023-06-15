# Generated by Django 4.1.7 on 2023-05-07 18:19

import ImageSRAPP.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ImageSRAPP', '0008_alter_image_table_sr_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image_table_sr',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sr_image', models.ImageField(null=True, upload_to=ImageSRAPP.models.file_path_sr)),
            ],
        ),
        migrations.RemoveField(
            model_name='image_table',
            name='sr_image',
        ),
        migrations.AlterField(
            model_name='image_table',
            name='lr_image',
            field=models.ImageField(null=True, upload_to=ImageSRAPP.models.file_path),
        ),
    ]