from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from events.models import Event, EventRegistration
from events.forms import EventForm
from django.contrib import messages

# Create your views here.
@login_required(login_url='/accounts/login')
def event_lists(request):
    events = Event.objects.all()
    is_registered = EventRegistration.objects.filter(user = request.user).exists()
    context = {'events':events, 'is_registered': is_registered}
    return render(request, 'events/index.html', context)

@login_required(login_url='/accounts/login')
def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Event created successfully')
            return redirect('/events')
    return render(request, 'events/create.html') # return eventCreation form

@login_required(login_url='/accounts/login')
def update_event(request, pk:int):
    try:
        event = Event.objects.get(pk=pk)
    except Event.DoesNotExist as error:
        return error
    form = EventForm(instance=event)
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            messages.success(request, 'Event updated successfully')
            return redirect('/events')
    return render(request, 'events/update.html', {'event': event}) # return eventCreation form with event instance

@login_required(login_url='/accounts/login')
def delete_event(request, pk:int):
    try:
        event = Event.objects.get(pk=pk)
    except Event.DoesNotExist as error:
        return error
    event.delete()
    messages.success(request, 'Event deleted successfully')
    return redirect('/events') # redirect to events

@login_required(login_url='/accounts/login')
def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    is_registered = EventRegistration.objects.filter(user=request.user, event=event_id).exists()
    
    context = {
        'event': event,
        'is_registered': is_registered,
    }
    return render(request, 'events/event_detail.html', context)

@login_required(login_url='/accounts/login')
def event_registration(request, event_id):
    """
        Users event registration
    """
    event = get_object_or_404(Event, id=event_id)
    EventRegistration.objects.get_or_create(user=request.user, event=event)
    return redirect('events:event_detail', event_id=event_id)

@login_required(login_url='/accounts/login')
def cancel_registration(request, event_id):
    """
        Cancel event registration
    """
    event = get_object_or_404(Event, id=event_id)
    EventRegistration.objects.filter(user=request.user, event=event).delete()
    return redirect('events:event_detail', event_id=event_id)

@login_required(login_url='/accounts/login')
def registrations(request):
    event_registrations = EventRegistration.objects.select_related('user', 'event').all().exclude(user=request.user)
    context = {
        'event_registrations': event_registrations
    }
    return render(request, 'events/registration.html', context)
    
        