# Generated by Django 3.2 on 2021-05-10 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_2_process_instrument', '0004_alter_homeimageslider_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('Qualification', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=300)),
            ],
        ),
    ]
