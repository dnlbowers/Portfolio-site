# Generated by Django 3.2 on 2022-07-24 01:05

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('client_projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientproject',
            name='id',
            field=models.UUIDField(
                default=uuid.uuid4,
                editable=False,
                primary_key=True,
                serialize=False,
                unique=True),
        ),
    ]
