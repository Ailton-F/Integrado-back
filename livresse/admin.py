from django.contrib import admin
from livresse.models import User

# Register your models here.

class Users(admin.ModelAdmin):
    list_display = ('id', 'name', 'email')
    list_display_links = ('email',)
    search_fields = ('name',)

admin.site.register(User, Users)