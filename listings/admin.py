from django.contrib import admin
from listings.models import Project
from listings.models import Language
from listings.models import Framework


admin.site.register(Project)
admin.site.register(Language)
admin.site.register(Framework)