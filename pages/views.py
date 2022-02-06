from random import random
import re
import base64
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
import pathlib
from utils import convert_to_video, fetch_emotions, fetch_out, parse_and_process, plot_emotions, random

# Create your views here.
# takes request -> response
# response handlers
# current_path = pathlib.Path().resolve()

@csrf_exempt 
def homepage_view(request):
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
        global url
        url = fetch_out(topemotion)
        #print(url) # url contains link to spotify playlist
    return render(request, 'HTMLFrontPage.html') #takes in template name and context

def say_hello(request):
    return render(request, 'hello.html', {'name': 'facenovel'}) # name is an input vbl to the view

def happy_view(request):
    return render(request, 'happy.html', {  'link': url,}) # name is an input vbl to the view
def sad_view(request):
    c = pathlib.Path().resolve()/"/images/Animals"
    print(c)
    url="test"
    return render(request, 'sad.html',   {   'link': url,
                                            'img_link': c / str(random.randint(1,5))})
def angry_view(request):
    return render(request, 'angry.html', {  'link': url})

def fear_view(request):
    # d = "C:\Users\andyw\OneDrive\Documents\GitHub\ICHack_Project\images\Nature"
    return render(request, 'fear.html', {  'link': url,
                                            'img_link': str(random.randint(1,5))})
