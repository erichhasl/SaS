from django.contrib import admin
from .models import Betrieb, Partei, PresidentCandidate, Question
from startpage.models import Banned
from django.contrib.admin import helpers
from django.shortcuts import render
from django.template.defaulttags import register


@register.filter
def get_item(dictionary, key):
        return dictionary.get(key)


def ban_ip(modeladmin, request, queryset):
    for obj in queryset:
        banned = Banned(ip_address=obj.ip_address,
                        reason="")
        banned.save()
    modeladmin.message_user(request, "Ausgewählte Urheber erfolgreich verbannt.")
ban_ip.short_description = "Urheber ausgewählter Eintrage verbannen"


def create_overview(modeladmin, request, queryset):
    if request.POST.get('back'):
        pass
    else:
        raummap = {}
        for b in queryset:
            if b.raum in raummap:
                raummap[b.raum]["anzahl"] += 1
                raummap[b.raum]["belegung"] += b.raumforderung
            else:
                raummap[b.raum] = {"anzahl": 1, "belegung": b.raumforderung}
        context = {'action_checkbox_name': helpers.ACTION_CHECKBOX_NAME,
                   'betriebe': queryset,
                   'arbeitnehmer_gesamt': sum([b.arbeitnehmerzahl for b in
                                               queryset]),
                   'raummap': raummap,
                   'title': "Betriebsübersicht"}
        return render(request, 'meingoethopia/betriebe_overview.html', context)

create_overview.short_description = "Übersicht erstellen"


# Register your models here.
class BetriebAdmin(admin.ModelAdmin):
    list_display = ('name', 'manager', 'aufsicht', 'raum',
                    'arbeitnehmerzahl_kurz', 'confirmed',
                    'approved')
    list_filter = ('confirmed', 'approved', 'raum')
    search_fields = ('name', 'manager', 'raum', 'aufsicht')
    actions = [ban_ip, create_overview]


class ParteiAdmin(admin.ModelAdmin):
    list_display = ('name', 'abbreviation', 'chef', 'description', 'confirmed',
                    'approved')
    list_filter = ('confirmed', 'approved')
    actions = [ban_ip]


class PresidentAdmin(admin.ModelAdmin):
    list_display = ('name', 'confirmed', 'approved')
    list_filter = ('confirmed', 'approved')
    actions = [ban_ip]


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('subject', 'answered')
    list_filter = ('answered',)
    actions = [ban_ip]

admin.site.register(Betrieb, BetriebAdmin)
admin.site.register(Partei, ParteiAdmin)
admin.site.register(PresidentCandidate, PresidentAdmin)
admin.site.register(Question, QuestionAdmin)
