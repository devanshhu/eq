from django.contrib import admin
from .models import AppUser
# Register your models here.


class UserAdminPanel(admin.ModelAdmin):
    list_display = ['name', 'enrollmentno']
    list_display_links = ['name']

    class Meta:
        model = AppUser


admin.site.register(AppUser, UserAdminPanel)
