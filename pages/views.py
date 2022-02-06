import re
import base64
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
# takes request -> response
# response handlers

@csrf_exempt 
def homepage_view(request):
    image = request.POST.get('imgBase64')
    if image:
        image_list_bytes = json.loads(image)
        image_list = []
        for image in image_list_bytes:
                image = image.split(',')
                image_list.append(base64.b64decode((image[1])))
    return render(request, 'HTMLFrontPage.html') #takes in template name and context

def say_hello(request):
    return render(request, 'hello.html', {'name': 'facenovel'}) # name is an input vbl to the view

def happy_view(request):
    return render(request, 'happy.html', {'link': 'test_link'}) # name is an input vbl to the view