from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Event

# Create your views here.
class EventsList(generic.ListView):
    """View for listing all events.

    Args:
        generic (_type_): _description_
    """


    model = Event
    template_name = "index.html"
    paginate_by = 12


def event_detail(request, event_id):
    """View for displaying the details of a specific event.

    Args:
        request (_type_): _description_
        event_id (_type_): _description_

    Returns:
        _type_: _description_
    """

    # Database request
    queryset = Event.objects.all()
    event = get_object_or_404(queryset, event_id=event_id)

    return render(
        request,
        "events/event_detail.html",
        {"event": event}
    )