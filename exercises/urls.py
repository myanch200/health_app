from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
app_name = "exercises"
urlpatterns = [
    path('', views.exercise, name='exercise'),
    path('articles/<pk>',views.exercise_detail, name='exercise_detail'),
   
]

urlpatterns += static(settings.MEDIA_URL,document_root= settings.MEDIA_ROOT)
