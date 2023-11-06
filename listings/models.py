from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=2000)
    language = models.CharField(max_length=50)
    isFinish = models.BooleanField(default=False)
    features = models.CharField(max_length=10000)
    logo = models.ImageField(upload_to='images')
    gitHubLink = models.URLField()
    viewsLink = models.URLField()
    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.fields.CharField(max_length=100)
    maitrise = models.fields.IntegerField(
    validators=[MinValueValidator(0), MaxValueValidator(100)]
    )
    logo = models.fields.TextField()
    def __str__(self):
        return f'{self.name}'

class Framework(models.Model):
    name = models.fields.CharField(max_length=100)
    maitrise = models.fields.IntegerField(
    validators=[MinValueValidator(0), MaxValueValidator(100)]
    )
    logo = models.fields.TextField(max_length=3000)
    def __str__(self):
        return f'{self.name}'