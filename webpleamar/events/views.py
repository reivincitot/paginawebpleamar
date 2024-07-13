from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import ClubEvent
import json

def event_list(request):
    events = ClubEvent.objects.all()
    return render(request, 'events/event_list.html', {'events': events})

def event_detail(request, id):
    event = ClubEvent.objects.get(id=id)
    return render(request, 'events/event_detail.html', {'event': event})

def calendar_view(request):
    return render(request, 'events/calendar.html')

@csrf_exempt
def add_event(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        title = data.get('title')
        time = data.get('time')
        description = data.get('description')
        day = data.get('day')
        month = data.get('month')
        year = data.get('year')

        event = ClubEvent.objects.create(
            titulo=title,
            start_time=time,
            descripcion=description,
            day=day,
            month=month,
            year=year
        )
        return JsonResponse({'message': 'Event added successfully'}, status=201)

    return JsonResponse({'error': 'Invalid request method'}, status=405)
