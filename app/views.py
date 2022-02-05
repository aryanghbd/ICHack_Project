from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# takes request -> response
# response handlers
def say_hello(request):
    return render(request, 'hello.html', {'name': 'facenovel'}) # name is an input vbl to the view
