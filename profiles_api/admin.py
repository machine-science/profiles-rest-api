from django.contrib import admin

# Register your models here.
from profiles_api import models

# This tells django admin to register our user profile model with the admin site
# so it makes accessible through admin interface
admin.site.register(models.UserProfile)
