# Generated by Django 3.2 on 2021-05-07 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_2_process_instrument', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instrumentsparameterswise',
            name='bootstrap_icons',
            field=models.CharField(blank=True, help_text='<h4>do not play with this, this part is related to coding </h4>', max_length=100),
        ),
    ]
