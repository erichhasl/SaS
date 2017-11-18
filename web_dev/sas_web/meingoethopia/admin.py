from django.contrib import admin
from .models import Betrieb, Partei, PresidentCandidate


# Register your models here.
class BetriebAdmin(admin.ModelAdmin):
    list_display = ('name', 'manager', 'confirmed')
    list_filter = ('confirmed',)


class ParteiAdmin(admin.ModelAdmin):
    list_display = ('name', 'abbreviation', 'chef', 'description', 'confirmed')
    list_filter = ('confirmed',)


class PresidentAdmin(admin.ModelAdmin):
    list_display = ('name', 'confirmed')
    list_filter = ('confirmed',)

admin.site.register(Betrieb, BetriebAdmin)
admin.site.register(Partei, ParteiAdmin)
admin.site.register(PresidentCandidate, PresidentAdmin)
