from django.contrib import admin
from .models import Betrieb, Partei, PresidentCandidate, Question, Angestellter,\
    Aufsicht, Betriebsaufsicht
from startpage.models import Banned
from django.contrib.admin import helpers
from django.shortcuts import render
from django.template.defaulttags import register
from django.db import models
from django import forms
from easy_select2 import apply_select2


class ZugeteiltFilter(admin.SimpleListFilter):
    title = 'Zugeteilt'
    parameter_name = 'zugeteilt'
    default_value = ('Alle', None)

    def lookups(self, request, model_admin):
        return (
            ('Alle', 'Alle'),
            ('True', 'Zugeteilt'),
            # ('More', 'Mehrfach zugeteilt'),
            ('False', 'Nicht zugeteilt'),
        )

    def queryset(self, request, queryset):
        if self.value() == 'True':
            print("filter auf true")
            return queryset.filter(betriebe__gt=0).distinct()
        elif self.value() == 'False':
            print("filter auf false")
            return queryset.filter(betriebe__exact=None).distinct()
        elif self.value() is None:
            return queryset
        elif self.value() == 'All':
            return queryset

    def choices(self, cl):
        for lookup, title in self.lookup_choices:
            yield {
                'selected':
                    self.value() == lookup or
                    (self.value() is None and lookup == self.default_value[0]),
                'query_string': cl.get_query_string({
                                    self.parameter_name:
                                    lookup,
                                }, []),
                'display': title
            }


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
                   'title': "Betriebsübersicht",
                   'kreditgesamt': sum([b.kredit for b in queryset])}
        return render(request, 'meingoethopia/betriebe_overview.html', context)

create_overview.short_description = "Übersicht erstellen"


class AufsichtInline(admin.TabularInline):
    model = Betriebsaufsicht
    extra = 0
    formfield_overrides = {
        models.ManyToManyField: {'widget': forms.CheckboxSelectMultiple},
        models.ForeignKey: {'widget': apply_select2(forms.Select)}
    }


# Register your models here.
class BetriebAdmin(admin.ModelAdmin):
    list_display = ('name', 'manager', 'show_aufsichten', 'raum',
                    'arbeiter_effektiv', 'punkt',
                    'approved', 'beaufsichtigt')
    list_filter = ('confirmed', 'approved', 'raum')
    search_fields = ('name', 'manager', 'raum', 'aufsicht')
    formfield_overrides = {
        models.ManyToManyField: {'widget': forms.CheckboxSelectMultiple},
        models.ForeignKey: {'widget': apply_select2(forms.Select)}
    }
    actions = [ban_ip, create_overview]
    filter_horizontal = ('angestellte',)
    inlines = [AufsichtInline]


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


class AngestellterAdmin(admin.ModelAdmin):
    list_display = ('name', 'klasse', 'is_teacher', 'show_betriebe', 'zugeteilt')
    list_filter = (ZugeteiltFilter,)
    search_fields = ('name', 'klasse')


class AufsichtAdmin(admin.ModelAdmin):
    list_display = ('name', 'show_stunden')
    search_fields = ('name',)
    formfield_overrides = {
        models.ManyToManyField: {'widget': forms.CheckboxSelectMultiple},
        models.ForeignKey: {'widget': apply_select2(forms.Select)}
    }

admin.site.register(Betrieb, BetriebAdmin)
admin.site.register(Partei, ParteiAdmin)
admin.site.register(PresidentCandidate, PresidentAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Angestellter, AngestellterAdmin)
admin.site.register(Aufsicht, AufsichtAdmin)
