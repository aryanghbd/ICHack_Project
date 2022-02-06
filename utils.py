from fer import Video
from fer import FER
import os
import sys
import pandas as pd
import cv2
import numpy as np
import glob
import random
import requests
import json
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


def convert_to_video(filepath):
    ##Given a filepath containing the images received from the backend, generate an mp4 video
    img_array = []
    for filename in sorted(glob.glob(filepath)):
        print(filename)
        img = cv2.imread(filename)
        height, width, layers = img.shape
        size = (width, height)
        img_array.append(img)

    out = cv2.VideoWriter('output/out.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 10, size)

    for i in range(len(img_array)):
        out.write(img_array[i])
    out.release()
    print("Video generated")
    return 0

def parse_and_process(video_location):
    face_detector = FER(mtcnn=True)
    input_video = Video(video_location)
    analyzed_data = input_video.analyze(face_detector, display=False)
    vid_df = input_video.to_pandas(analyzed_data)
    vid_df = input_video.get_first_face(vid_df)
    vid_df = input_video.get_first_face(vid_df)
    return vid_df

def parse_and_process(video_location):
    face_detector = FER(mtcnn=True)
    input_video = Video(video_location)
    analyzed_data = input_video.analyze(face_detector, display=False)
    vid_df = input_video.to_pandas(analyzed_data)
    vid_df = input_video.get_first_face(vid_df)
    vid_df = input_video.get_first_face(vid_df)
    return vid_df

def plot_emotions(data):
    pltfig = data.plot(figsize=(20, 8), fontsize=16).get_figure()


def fetch_emotions(vid_df):
    angry = sum(vid_df.angry)
    disgust = sum(vid_df.disgust)
    fear = sum(vid_df.fear)
    happy = sum(vid_df.happy)
    sad = sum(vid_df.sad)
    surprise = sum(vid_df.surprise)
    neutral = sum(vid_df.neutral)
    # Populate emotion values

    emotions = ['Angry', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral']
    emotions_values = [angry, disgust, fear, happy, sad, surprise, neutral]
    topemotions = sorted(emotions_values)
    prominent_emotion = emotions[emotions_values.index(topemotions[-1])]
    score_comparisons = pd.DataFrame(emotions, columns=['Human Emotions'])
    score_comparisons['Emotion Value from the Video'] = emotions_values
    return score_comparisons, prominent_emotion

#Authentication - without user
client_credentials_manager = SpotifyClientCredentials(client_id='d732ba776cb54bf681ec10673a7dfe5f', client_secret='af80ba1c481f48d69ffbebb817dfcdcc')
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

def make_lists(s):
    out = []
    tmp = sp.category_playlists(s,'GB',5,0)
    links = tmp['playlists']['items']
    for link in links:
        out.append(link['external_urls']['spotify'])
    return out

def fetch_out(feel):
    pop_l = make_lists('pop')
    blues_l = make_lists('blues')
    chill_l = make_lists('chill')
    rnb_l = make_lists('rnb')
    funk_l = make_lists('funk')
    songlists = {"Happy":pop_l,
                "Sad":blues_l,
                "Angry":chill_l,
                "Fear":rnb_l,
                "Surprise":funk_l,
                }
    return songlists[feel][random.randint(0,len(songlists[feel])-1)]

#def jokes(f):
    #data = requests.get(f)
    #tt = json.loads(data.text)
    #return tt

#def joke():
    #f = r"https://official-joke-api.appspot.com/random_joke"
    #a = jokes(f)
    #j = a[0]
    #return (j["setup"],j["punchline"])

if "__name__" == "__main__":
    convert_to_video('Images/*.jpg')
    vid_df = parse_and_process("out.mp4")
    plot_emotions(vid_df)
    scores, topemotion = fetch_emotions(vid_df)
    print(scores)