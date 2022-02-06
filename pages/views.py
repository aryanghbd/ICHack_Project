import re
import base64
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

from utils import convert_to_video, fetch_emotions, fetch_out, parse_and_process, plot_emotions

# Create your views here.
# takes request -> response
# response handlers

@csrf_exempt 
def get_url(request):
    image = request.POST.get('imgBase64')
    if image:
        image_list_bytes = json.loads(image)
        for idx,image in enumerate(image_list_bytes):
            image = image.split(',')
            file = open(f'output/Images/{idx}.jpg', 'wb')
            file.write(base64.b64decode((image[1])))
            file.close()
        convert_to_video('output/Images/*.jpg')
        vid_df = parse_and_process("output/out.mp4")
        plot_emotions(vid_df)
        scores, topemotion = fetch_emotions(vid_df)
        url = fetch_out(topemotion)
    return url
def homepage_view(request):    
        #print(url) # url contains link to spotify playlist
    return render(request, 'HTMLFrontPage.html') #takes in template name and context

def say_hello(request):
    return render(request, 'hello.html', {'name': 'facenovel'}) # name is an input vbl to the view

def happy_view(request):
    return render(request, 'happy.html', {  'link': get_url(request),
                                            'joke': 'test_joke'}) # name is an input vbl to the view
def sad_view(request):
    return render(request, 'sad.html',   {   'link': 'test_link',
                                            'img_link':'https://images.unsplash.com/photo-1615751072497-5f5169febe17?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MXx8Y3V0ZSUyMGRvZ3xlbnwwfHwwfHw%3D&w=1000&q=80'}) # name is an input vbl to the view
def angry_view(request):
    return render(request, 'angry.html', {  'link': 'test_link'})

def fear_view(request):
    return render(request, 'fear.html', {  'link': 'test_link'})