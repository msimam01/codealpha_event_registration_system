from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from events.models import Event, EventRegistration
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash
from event_management_system.forms import UserChangeForm, UserPasswordChangeForm
from django.contrib import messages


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


@login_required(login_url='/accounts/login')
def profile(request):
    if request.method == "POST":
        form = UserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
            return redirect('/profile', form)
    form = UserChangeForm(request.user)
    p_form = UserPasswordChangeForm(request.user)
    return render(request, 'profile.html', {'form':form, 'p_form': p_form})

@login_required(login_url='/account/login')
def change_password(request):
    if request.method == "POST":
        form = UserPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was updated successfully') # redirect with success message
            return redirect('/profile')
        else:
          return render(request, 'profile.html', {'p_form': form})
    else:
        form = UserChangeForm(request.user)
        p_form = UserPasswordChangeForm(request.user)
        return redirect('/profile', {'form':form, 'p_form': p_form})


