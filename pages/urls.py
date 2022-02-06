from django.urls import path
from pages import views

# URL configurations
urlpatterns = [
    path('hello/', views.say_hello)
]