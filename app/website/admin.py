from django.contrib import admin
# Register your models here.

from .models import Event, Flyer, ThemeColor

class FlyerInline(admin.TabularInline):
    model = Flyer

class EventAdmin(admin.ModelAdmin):
    fields = ('name', 'theme_color', 'event_date', 'publish_date')
    list_display = ['name']
    inlines = [FlyerInline]

class ThemeColorAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Event, EventAdmin)
admin.site.register(ThemeColor, ThemeColorAdmin)