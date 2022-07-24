from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

import uuid

# Create your models here.
class ClientProject(models.Model):
    project_id = models.CharField(max_length=32, null=False, editable=False, unique=True)
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    Summary = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField(blank=True, null=True)
    grant_access_to = models.ManyToManyField(User, related_name="permitted_to_access")
    
    def __str__(self):
        return self.name

    def _generate_project_id(self):
        """
        Generate a random, unique order number using UUID
        """
        return uuid.uuid4().hex.upper()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        if not self.project_id:
            self.project_id = self._generate_project_id()
        super().save(*args, **kwargs)


class Requirements(models.Model):
    project = models.ForeignKey(ClientProject, on_delete=models.CASCADE)
    design_document = models.BooleanField(default=False)
    wireframes_design = models.BooleanField(default=False)
    mockup_design = models.BooleanField(default=False)
    official_document = models.BooleanField(default=False)
    front_end = models.BooleanField(default=False)
    back_end = models.BooleanField(default=False)
    deployment = models.BooleanField(default=False)
    hosting = models.BooleanField(default=False)
    domain = models.BooleanField(default=False)
    maintenance = models.BooleanField(default=False)



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
    deployed_url = models.URLField(max_length=2000, blank=True, null=True)