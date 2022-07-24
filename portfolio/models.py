from django.db import models

# Create your models here.
STATUS = ((0, 'hidden'), (1, 'Public'), (2, 'coming soon'))
TYPE = ((0, 'website'), (1, 'app'), (2, 'game'), (3, 'other'))


class Project(models.Model):
    """"
    Holds project details in DB.
    """

    title = models.CharField(max_length=200)
    description = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    hosted_url = models.URLField(max_length=200, blank=True)
    repo_url = models.URLField(max_length=200, blank=True)
    screenshot = models.ImageField(
        upload_to='portfolio-screenshots/', blank=True)
    completion_date = models.DateField(blank=True, null=True)
    project_type = models.IntegerField(choices=TYPE, default=0)

    class meta:
        ordering = ['-completion_date']
        verbose_name_plural = 'projects'

    def __str__(self):
        return self.title
