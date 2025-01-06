from django.urls import path
from . import views

app_name = 'events'

urlpatterns = [
    path('', views.event_lists, name='events'),
    path('registrations', views.registrations, name='registrations'),
    path('create/', views.create_event, name='create'),
    path('update/<int:pk>/', views.update_event, name='update'),
    path('delete/<int:pk>/', views.delete_event, name='delete'),
    
    # event registration routes
    path('<int:event_id>/', views.event_detail, name="event_detail"),
    path('<int:event_id>/register/', views.event_registration, name="event_registration"),
    path('<int:event_id>/cancel/', views.cancel_registration, name='cancel_registration'),
]
