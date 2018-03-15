from django.contrib import admin
from .models import ParteiWerbung, PraesidentWerbung, ParteiAnhang, \
    PraesidentAnhang, Parlamentssitzung, SitzungsKind


class ParteiAnhangInline(admin.TabularInline):
    model = ParteiAnhang
    extra = 0


class PraesidentAnhangInline(admin.TabularInline):
    model = PraesidentAnhang
    extra = 0


class ParteiWerbungAdmin(admin.ModelAdmin):
    list_display = ('partei',)
    inlines = [ParteiAnhangInline]


class PraesidentWerbungAdmin(admin.ModelAdmin):
    list_display = ('praesident',)
    inlines = [PraesidentAnhangInline]


class ParlamentssitzungAdmin(admin.ModelAdmin):
    list_display = ('date', 'stunde', 'raum', 'kind')


class SitzungsKindAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(ParteiWerbung, ParteiWerbungAdmin)
admin.site.register(PraesidentWerbung, PraesidentWerbungAdmin)
admin.site.register(Parlamentssitzung, ParlamentssitzungAdmin)
admin.site.register(SitzungsKind, SitzungsKindAdmin)
