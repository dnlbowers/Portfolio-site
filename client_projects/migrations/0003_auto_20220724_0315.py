# Generated by Django 3.2 on 2022-07-24 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client_projects', '0002_alter_clientproject_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientproject',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='clientproject',
            name='slug',
            field=models.SlugField(max_length=255),
        ),
    ]
