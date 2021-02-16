from django.db import models

# Create your models here.


class Event(models.Model):
    """describes an event"""
    name = models.CharField('event name', max_length=256)
    publish_date = models.DateTimeField('date on which to make the event public')
    event_date = models.DateTimeField('date/time of the event')


class Flyer(models.Model):
    """describes a flyer associated with an event"""
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    image = models.ImageField('Flyer image')
