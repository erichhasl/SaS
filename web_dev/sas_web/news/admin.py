from django.contrib import admin
from .models import ParteiWerbung


# Register your models here.
class ParteiWerbungAdmin(admin.ModelAdmin):
    list_display = ('partei',)

admin.site.register(ParteiWerbung, ParteiWerbungAdmin)
