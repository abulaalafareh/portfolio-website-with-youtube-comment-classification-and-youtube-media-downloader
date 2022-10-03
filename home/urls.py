from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [

    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('projects', views.projects, name='projects'),
    path('ytcc', views.ytcc, name='ytcc'),
    path('ytmd', views.ytmd, name='ytmd'),
    path('ytmd_function', views.ytmd_function, name='ytmd_function'),
    path('contact', views.contact, name='contact'),
    path('sentiment_analysis', views.sentiment_analysis, name='sentiment_analysis'),
    # path('complete_aud_download', views.complete_aud_download, name='complete_aud_download'),
    # path('complete_vid_download', views.complete_vid_download, name='complete_vid_download'),

]
