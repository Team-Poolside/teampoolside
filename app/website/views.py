from datetime import timedelta
from django.http import HttpResponse
from django.http.request import HttpRequest
from django.shortcuts import render
from django.utils import timezone

from .models import Event, Flyer


def index(request: HttpRequest):
    # get all still ongoing events in the database whose publish dates have past and pass them to the view
    return HttpResponse(render(request, 'website/index.html', {
        'events': [
            (event, Flyer.objects.filter(event__name=event.name))
            for event in list(Event.objects.all().filter(publish_date__lte=timezone.now()).order_by('event_date'))
            if timezone.now() < event.event_date + timedelta(days=1)
        ],
        'colors': {
            'yuleside_red': '#6e001a',
            'wavepool_pink': '#9e0a8e',
            'poolside_blue': '#005182',
        },
    }))
