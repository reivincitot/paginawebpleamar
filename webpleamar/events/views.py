from django.views.generic import TemplateView


class CalendarView(TemplateView):
    template_name = 'events/calendar.html'


def club_calendar_view(request):
    view = CalendarView.as_view()
    return view(request)
