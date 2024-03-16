from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.


class PersonalData(models.Model):
    full_name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return f"{self.full_name}"


class WorkExperience(models.Model):
    company_name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    year = models.IntegerField(default=2000)
    description = RichTextField(null=True)

    def __str__(self):
        return f"{self.company_name}"


class Projects(models.Model):
    project_name = models.CharField(max_length=200)
    project_description = models.TextField()
    project_link = models.URLField()

    def __str__(self):
        return f"{self.project_name}"
