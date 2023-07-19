from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime

class Goal(models.Model):
    date = models.DateField(default=datetime.now)
    name = models.CharField(max_length=200)
    isComplete = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}, {self.date}, {self.user}"

    def toDictionary(self):
        return {
            "date": self.date.isoformat(),
            "name": self.name,
            "isComplete": self.isComplete
        }
    
class Workout(models.Model):
    date = models.DateField(default=datetime.now)
    distance = models.CharField(max_length=200)
    pace = models.CharField(max_length=200)
    strengthCircuit = ArrayField(models.CharField(max_length=200), default=list)
    mobilityChallenge = ArrayField(models.CharField(max_length=200), default=list)
    videos = ArrayField(models.CharField(max_length=200), default=list)
    user = models.ForeignKey(User, models.CASCADE)

    def __str__(self):
        return f"{self.distance}, {self.effort}, {self.user}"
    
    def toDictionary(self):
        return {
            "date": self.date.isoformat(),
            "distance": self.distance,
            "effort": self.effort,
            "strengthCircuit": self.strengthCircuit,
            "mobilityChallenge": self.mobilityChallenge,
            "strengthChallenge": self.strengthChallenge,
            "videos": self.videos
        }

class Race(models.Model):
    date = models.DateField(default=datetime.now)
    name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name} - {self.date}"
    
    def toDictionary(self):
        return {
            "date": self.date.isoformat(),
            "name": self.name
        }

