from django.urls import path
from . import views

urlpatterns = [
    path("authenticate/", views.authenticate, name="authenticate"),
    path("fetchUserData/", views.fetchUserData, name="fetchUserData"),
    path("fetchUpcomingRaces/", views.fetchUpcomingRaces, name="fetchUpcomingRaces"),
    path("updateUserGoals/", views.updateUserGoals, name="updateUserGoals"),
    path("fetchCSRFToken/", views.fetchCSRFToken, name="fetchCSRFToken")
]