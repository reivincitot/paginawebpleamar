from django.shortcuts import render
from .models import ClubEvent

def event_list(request):
    events = ClubEvent.objects.all()
    return render(request, 'events/event_list.html', {'events': events})

def event_detail(request, id):
    event = ClubEvent.objects.get(id=id)
    return render(request, 'events/event_detail.html', {'event': event})

def calendar_view(request):
    return(render,'events/calendar.html')
