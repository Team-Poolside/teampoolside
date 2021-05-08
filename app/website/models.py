from django.db import models
from django.forms.widgets import Input

# Create your models here.

class ColorWidget(Input):
    input_type = 'color'
    template_name = 'website/forms/widgets/color.html'


class ColorField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 10
        super().__init__(*args, **kwargs)
    
    def formfield(self, **kwargs):
        kwargs['widget'] = ColorWidget
        return super().formfield(**kwargs)


class ThemeColor(models.Model):
    name = models.CharField('color name', max_length=256)
    color = ColorField('color', default='#005182')

    def __unicode__(self):
        return self.name
    
    def __str__(self):
        return self.name


class Event(models.Model):
    """describes an event"""
    name = models.CharField('event name', max_length=256)
    publish_date = models.DateTimeField('date on which to make the event public')
    event_date = models.DateTimeField('date/time of the event')
    theme_color = models.ForeignKey(ThemeColor, on_delete=models.DO_NOTHING, null=True)


class Flyer(models.Model):
    """describes a flyer associated with an event"""
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    image = models.ImageField('Flyer image')
