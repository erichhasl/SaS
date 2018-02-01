from django.contrib import admin
from .models import ParteiWerbung, PraesidentWerbung, ParteiAnhang, \
    PraesidentAnhang


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

# admin.site.register(ParteiWerbung, ParteiWerbungAdmin)
# admin.site.register(PraesidentWerbung, PraesidentWerbungAdmin)
