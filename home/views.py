from django.shortcuts import render

# Create your views here.
#Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
#venv\scripts\activate
from datetime import datetime
from home.models import contactme, sentiment, downloads
from django.contrib import messages
from django.shortcuts import render, HttpResponse
import subprocess
# import pandas as pd
# import numpy as np
import ktrain
from ktrain import text
import tensorflow as tf
from tensorflow.python.client import device_lib
# Create your views here.
def home(request):
       
    return render(request, 'home.html')
    
def projects(request):
       
    return render(request, 'projects.html')





def ytcc(request):
    return render(request, 'ytcc.html')


# YouTube Media Downloader Working
def ytmd(request):
    return render(request, 'ytmd.html')


def ytmd_function(request):
    if request.method=='POST':
        url = request.POST.get('url')

        start_time = request.POST.get('start_time')
        end_time = request.POST.get('end_time')
        id=url

        # Function for complete audio download
        if 'complete_aud_download' in request.POST:
            
            
            if url=='':
                print('no input')
            else:
                try:
                    print('Adio downloading...........')
                    subprocess.run(['youtube-dl' ,'--extract-audio' ,'--audio-format' ,'mp3' ,'--output', '"%(uploader)s%(title)s.%(ext)s"' ,id] )
                    print('Downloaded')
                except:
                    print('error')
            Download = downloads( url = url, start_time = start_time, 
            end_time = end_time, type = 'complete Audio' , Date = datetime.today())
            Download.save()
            url=''


        # Function for complete video Download
        elif 'complete_vid_download' in request.POST:
              
            
            if url=='':
                print('no input')
            else:    
                id=url
                print(url)
                try:
                    print('vidio downloading...........')
                    subprocess.run(['youtube-dl', '-f','bestvideo', id] )
                    print('Downloaded')
                except:
                    print('error')
            Download = downloads( url = url, start_time = start_time, 
            end_time = end_time, type = 'complete Video' , Date = datetime.today())
            Download.save()

    
        # Function for cut audio Download
        elif 'cut_aud_download' in request.POST:
            
            if url=='':
                print('no input')
            else:
                id=url
                
                out = subprocess.run(['youtube-dl','-g',id], capture_output=True) 
                
                st = out.stdout.splitlines()
                try:
                    print('Adio downloading...........')
                    subprocess.run(['ffmpeg','-ss',start_time,'-to',end_time,'-i' ,st[1], '-c', 'copy', 'out9.mkv'])
                    print('Downloaded')
                except:
                    print('error')
            Download = downloads( url = url, start_time = start_time, 
            end_time = end_time, type = 'Cut Audio' , Date = datetime.today())
            Download.save()


        # Function for cut video Download
        elif 'cut_vid_download' in request.POST:
            
            if url=='':
                print('no input')
            else:
                id=url
            
                out = subprocess.run(['youtube-dl','-g',id], capture_output=True) 
                
                st = out.stdout.splitlines()
                try:
                    print('Adio downloading...........')
                    subprocess.run(['ffmpeg','-ss',start_time,'-to',end_time,'-i' ,st[0], '-c', 'copy','ouyoyo.mp4'])
                    print('Downloaded')
                except:
                    print('error')

            Download = downloads( url = url, start_time = start_time, 
            end_time = end_time, type = 'Cut Video' , Date = datetime.today())
            Download.save()
    url = ''
    return render(request, 'ytmd.html')







def contact(request):
       if request.method == "POST":
              
              email = request.POST.get('email')
              name = request.POST.get('name')
              message = request.POST.get('message')
              print(email)
              print(name)
              print(message)

              contact = contactme(email = email, name=name ,  message = message , Date = datetime.today())
              contact.save()
              messages.success(request, 'Your message has been sent')

       return render(request, 'home.html')

def sentiment_analysis(request):
       if request.method == "POST":
              
              predictor_load = ktrain.load_predictor('/Saved_Model_12/ALL_CATEGORIES_MODEL')
              predictor_load.get_classes()
              sentence = request.POST.get('sentence')
              print(sentence)
              result = predictor_load.predict(sentence)  
              Sentiment = sentiment(sentence = sentence, Sentiment = result )
              Sentiment.save()

              

       return render(request, 'ytcc.html' , {'result':result})