from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
app_name = "meditation"
urlpatterns = [
    path('', views.meditation, name='meditation'),
    path('yoga/', views.yoga_main, name='yoga_main'),
    path('breathing/', views.breathing_app, name='breathing_app'),
    path('music-meditation/', views.music_meditation, name='music_meditation'),

    path('yoga/article/<pk>', views.yoga_detailed, name='yoga_detailed')

   
]
