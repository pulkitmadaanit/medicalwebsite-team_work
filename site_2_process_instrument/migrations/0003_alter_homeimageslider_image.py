# Generated by Django 3.2 on 2021-05-10 06:56

import django.core.files.storage
from django.db import migrations, models
import site_2_process_instrument.models


class Migration(migrations.Migration):

    dependencies = [
        ('site_2_process_instrument', '0002_alter_instrumentsparameterswise_bootstrap_icons'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homeimageslider',
            name='image',
            field=models.FileField(help_text='Enter image you want to display on the home page slider ', storage=django.core.files.storage.FileSystemStorage(base_url='/media/my_sell/', location='/home/sunil/workspace/pulkit/django_project/medicalwebsite-team_work/media/my_sell/'), upload_to=site_2_process_instrument.models.image_directory_path),
        ),
    ]
