from django.contrib import admin
from .models import Betrieb, Partei, PresidentCandidate, Question
from startpage.models import Banned


def ban_ip(modeladmin, request, queryset):
    for obj in queryset:
        banned = Banned(ip_address=obj.ip_address,
                        reason="")
        banned.save()
    modeladmin.message_user(request, "Ausgewählte Urheber erfolgreich verbannt.")
ban_ip.short_description = "Urheber ausgewählter Eintrage verbannen"


# Register your models here.
class BetriebAdmin(admin.ModelAdmin):
    list_display = ('name', 'manager', 'confirmed')
    list_filter = ('confirmed',)
    actions = [ban_ip]


class ParteiAdmin(admin.ModelAdmin):
    list_display = ('name', 'abbreviation', 'chef', 'description', 'confirmed')
    list_filter = ('confirmed',)
    actions = ('ban_ip',)


class PresidentAdmin(admin.ModelAdmin):
    list_display = ('name', 'confirmed')
    list_filter = ('confirmed',)
    actions = ('ban_ip',)


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('subject', 'answered')
    list_filter = ('answered',)
    actions = ('ban_ip',)

admin.site.register(Betrieb, BetriebAdmin)
admin.site.register(Partei, ParteiAdmin)
admin.site.register(PresidentCandidate, PresidentAdmin)
admin.site.register(Question, QuestionAdmin)
