from django.contrib import admin

from .models import Entry


# Register your models here.
class EntryAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'element')

admin.site.register(Entry, EntryAdmin)
