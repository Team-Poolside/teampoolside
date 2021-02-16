from django.contrib import admin
# Register your models here.

from .models import Event, Flyer

class FlyerInline(admin.TabularInline):
    model = Flyer

class EventAdmin(admin.ModelAdmin):
    fields = ('name', 'event_date', 'publish_date')
    list_display = ['name']
    inlines = [FlyerInline]

admin.site.register(Event, EventAdmin)