from django.urls import path
from .views import game

urlpatterns = [
    path("", game, name= "start_game"),
]