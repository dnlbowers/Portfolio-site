# Generated by Django 3.2 on 2022-07-23 10:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientProject',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(blank=True, max_length=255, unique=True)),
                ('Summary', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('due_date', models.DateField(blank=True, null=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('grant_access_to', models.ManyToManyField(related_name='permitted_to_access', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Requirements',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('design_document', models.BooleanField(default=False)),
                ('wireframes_design', models.BooleanField(default=False)),
                ('mockup_design', models.BooleanField(default=False)),
                ('official_document', models.BooleanField(default=False)),
                ('front_end', models.BooleanField(default=False)),
                ('back_end', models.BooleanField(default=False)),
                ('deployment', models.BooleanField(default=False)),
                ('hosting', models.BooleanField(default=False)),
                ('domain', models.BooleanField(default=False)),
                ('maintenance', models.BooleanField(default=False)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client_projects.clientproject')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectFiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Initial_contract', models.FileField(blank=True, null=True, upload_to='contract/')),
                ('addendum', models.FileField(blank=True, null=True, upload_to='addendum/')),
                ('wireframes', models.FileField(blank=True, null=True, upload_to='wireframes/')),
                ('color_mockup', models.FileField(blank=True, null=True, upload_to='color_mockup/')),
                ('planning_docs', models.FileField(blank=True, null=True, upload_to='planning_docs/')),
                ('official_docs', models.FileField(blank=True, null=True, upload_to='official_docs/')),
                ('repo_location', models.URLField(blank=True, max_length=2000, null=True)),
                ('deployed_url', models.URLField(blank=True, max_length=2000, null=True)),
                ('related_project', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='client_projects.clientproject')),
            ],
        ),
    ]