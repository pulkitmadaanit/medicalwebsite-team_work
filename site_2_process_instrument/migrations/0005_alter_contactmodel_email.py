# Generated by Django 3.2 on 2021-05-06 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_2_process_instrument', '0004_alter_homeimageslider_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactmodel',
            name='email',
            field=models.EmailField(max_length=50),
        ),
    ]
