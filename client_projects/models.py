from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

import uuid

# Create your models here.
class ClientProject(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField(blank=True, null=True)
    
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(ClientProject, self).save(*args, **kwargs)


class Requirements(models.Model):
    project = models.ForeignKey(ClientProject, on_delete=models.CASCADE)
    design_document = models.BooleanField(default=False)
    wireframe_design = models.BooleanField(default=False)
    mockup_design = models.BooleanField(default=False)
    offical_document = models.BooleanField(default=False)
    front_end = models.BooleanField(default=False)
    back_end = models.BooleanField(default=False)



# how to upload a file to the server: and store it in the database:?
class ProjectFiles(models.Model):
    related_project = models.ForeignKey(ClientProject, on_delete=models.CASCADE, blank=True, null=True)
    Initial_contract = models.FileField(upload_to='contract/', blank=True, null=True)
    addendum = models.FileField(upload_to='addendum/', blank=True, null=True) 
    wireframes = models.FileField(upload_to='wireframes/', blank=True, null=True)
    color_mockup = models.FileField(upload_to='color_mockup/', blank=True, null=True)
    planning_docs = models.FileField(upload_to='planning_docs/', blank=True, null=True)
    official_docs = models.FileField(upload_to='official_docs/', blank=True, null=True)
    repo_location =models.URLField(max_length=2000, blank=True, null=True)