import re
import base64
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

from utils import convert_to_video, fetch_emotions, fetch_out, parse_and_process, plot_emotions

# Create your views here.
# takes request -> response
# response handlers

@csrf_exempt
def homepage_view(request):
    return render(request, 'HTMLFrontPage.html') #takes in template name and context

@csrf_exempt
def get_emotion(request):
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
        print(url) # url contains link to spotify playlist
        print("received")
        print(topemotion)
    return render(request, f"{topemotion}.html", {'link': url})


def say_hello(request):
    return render(request, 'hello.html', {'name': 'facenovel'}) # name is an input vbl to the view

def happy_view(request):
    return render(request, 'happy.html', {'link': 'test_link'}) # name is an input vbl to the view