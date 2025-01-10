from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=200)
    max_participants = models.IntegerField()
    
    def __str__(self):
        return f"{self.title}"      
    
class EventRegistration(models.Model):
    user = models.ForeignKey(to=User, related_name='user', on_delete=models.CASCADE)
    event = models.ForeignKey(to=Event, related_name='event', on_delete=models.CASCADE)
    registration_date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.username} registered for {self.event}"
    
    
