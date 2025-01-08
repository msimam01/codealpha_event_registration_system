from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from events.models import Event, EventRegistration
from django.contrib.auth.models import User


# Create your views here.
@login_required(login_url='/accounts/login')
def home(request):
    users = User.objects.count()
    events = Event.objects.count()
    
    context = {
        'users': users,
        'events': events,
    }
    return render(request, 'index.html', context)
