from django.contrib import admin
from .models import ParteiWerbung, PraesidentWerbung


# Register your models here.
class ParteiWerbungAdmin(admin.ModelAdmin):
    list_display = ('partei',)


class PraesidentWerbungAdmin(admin.ModelAdmin):
    list_display = ('praesident',)

admin.site.register(ParteiWerbung, ParteiWerbungAdmin)
admin.site.register(PraesidentWerbung, PraesidentWerbungAdmin)
