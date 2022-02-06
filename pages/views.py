import re
import base64
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import pathlib
from utils import convert_to_video, fetch_emotions, fetch_out, parse_and_process, plot_emotions
import random
import os

# Create your views here.
# takes request -> response
# response handlers

@csrf_exempt
def homepage_view(request):
    return render(request, 'base.html') #takes in template name and context

@csrf_exempt
def get_emotion(request):
    image = request.POST.get('imgBase64')
    if image:
        file = open(f'output/Images/0.jpg', 'wb')
        file.write(base64.b64decode(image.split(',')[1]))
        file.close()
        convert_to_video('output/Images/*.jpg')
        vid_df = parse_and_process("output/out.mp4")
        plot_emotions(vid_df)
        scores, topemotion = fetch_emotions(vid_df)
        url = fetch_out(topemotion)
        print(url) # url contains link to spotify playlist
        print("received")
        print(topemotion)
        # if topemotion.lower()=="sad":
            # c = os.getcwd() + "/images/Animals"
            # print(c)
            # return render(request, "sad.html", {'link': url, 'image_url': c + str(random.randint(1,5))})
        return render(request, f"{topemotion.lower()}.html", {'link': url})


# def say_hello(request):
#     return render(request, 'hello.html', {'name': 'facenovel'}) # name is an input vbl to the view

# def happy_view(request):
#     return render(request, 'happy.html', {'link': 'test_link'}) # name is an input vbl to the view