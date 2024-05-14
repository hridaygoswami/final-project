from django.db import models

# Create your models here.
class services(models.Model):
    name = models.CharField(max_length=20)
    logo = models.ImageField()
    desc = models.CharField(max_length=500)
    link = models.URLField()

class collectedData(models.Model):
    project_url = models.URLField()
    project_extensions = models.TextField()

class newServices(models.Model):
     name = models.CharField(max_length=20)
     logo = models.ImageField()
     desc = models.CharField(max_length=500)
     link = models.URLField()