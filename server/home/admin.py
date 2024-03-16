from django.contrib import admin
from . import models

admin.site.register(models.User)
admin.site.register(models.Roles)
admin.site.register(models.Tikest)
admin.site.register(models.History)
