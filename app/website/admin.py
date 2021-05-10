from django.contrib import admin
# Register your models here.

from .models import Event, Teaser, ThemeColor, Setlist


def flyer_inline(clazz):
    class FlyerInline(admin.TabularInline):
        model = clazz
    
    return FlyerInline


class EventAdmin(admin.ModelAdmin):
    fields = ('name', 'theme_color', 'event_date', 'publish_date')
    list_display = ['name']
    inlines = [flyer_inline(Teaser), flyer_inline(Setlist)]


class ThemeColorAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Event, EventAdmin)
admin.site.register(ThemeColor, ThemeColorAdmin)