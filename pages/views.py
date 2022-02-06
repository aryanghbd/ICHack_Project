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
    return render(request, 'happy.html', {  'link': 'test_link',
                                            'joke': 'test_joke'}) # name is an input vbl to the view
def sad_view(request):
    return render(request, 'sad.html',   {   'link': 'test_link',
                                            'img_link':'https://images.unsplash.com/photo-1615751072497-5f5169febe17?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MXx8Y3V0ZSUyMGRvZ3xlbnwwfHwwfHw%3D&w=1000&q=80'}) # name is an input vbl to the view
def angry_view(request):
    return render(request, 'angry.html', {  'link': 'test_link'})

def fear_view(request):
    return render(request, 'fear.html', {  'link': 'test_link'})