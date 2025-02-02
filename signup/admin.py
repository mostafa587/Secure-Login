from django.contrib import admin
from .models import User
# Register your models here.

admin.site.register(User) # This will allow the User model to be managed from the admin panel
