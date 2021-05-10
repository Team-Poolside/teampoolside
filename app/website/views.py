from datetime import timedelta
from django.http import HttpResponse
from django.http.request import HttpRequest
from django.shortcuts import render
from django.utils import timezone

from .models import Event, Setlist, Teaser


def is_active(event):
    return event.event_date < timezone.now() < event.event_date + timedelta(days=1)

def index(request: HttpRequest):
    # get all still ongoing events in the database whose publish dates have past and pass them to the view
    return HttpResponse(render(request, 'website/index.html', {
        'events': [
            # (event, flyer, setlist, is_active)
            (event, Teaser.objects.filter(event__name=event.name), Setlist.objects.filter(event__name=event.name), is_active(event))
            for event in list(Event.objects.all().filter(publish_date__lte=timezone.now()).order_by('event_date'))
            if timezone.now() < event.event_date + timedelta(days=1)
        ],
        'active_event': next(iter([event for event in list(Event.objects.all().order_by('event_date')) if is_active(event)]), None),
    }))
