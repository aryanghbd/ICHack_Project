from fer import Video
from fer import FER
import os
import sys
import pandas as pd
import cv2

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
    emotions = ['Angry', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral']
    emotions_values = [angry, disgust, fear, happy, sad, surprise, neutral]
    prominent_emotion = emotions[emotions_values.index(max(emotions_values))]
    score_comparisons = pd.DataFrame(emotions, columns = ['Human Emotions'])
    score_comparisons['Emotion Value from the Video'] = emotions_values
    return score_comparisons, prominent_emotion

vid_df = parse_and_process("testbest.mp4")
plot_emotions(vid_df)
fetch_emotions(vid_df)