from django.contrib import admin
from .models import PersonalData, WorkExperience, Projects

admin.site.register([PersonalData, Projects, WorkExperience])

# Register your models here.
