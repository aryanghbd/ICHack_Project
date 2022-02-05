from django.urls import path
from . import views

# URL configurations
urlpatterns = [
    path('hello/', views.say_hello)
]