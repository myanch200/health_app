from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
app_name = "nutrition_planner"
urlpatterns = [
    path('', views.nutrition_planner, name='nutrition_planner'),
    path('recipe/<pk>', views.detailed_recipe, name='detailed_recipe'),

   
]
urlpatterns += static(settings.MEDIA_URL,document_root= settings.MEDIA_ROOT)