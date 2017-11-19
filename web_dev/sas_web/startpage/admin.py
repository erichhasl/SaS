from django.contrib import admin
from .models import Banned


class BanAdmin(admin.ModelAdmin):
    list_display = ('ip_address', 'reason')

# Register your models here.
admin.site.register(Banned, BanAdmin)
