from django.urls import path, include
from gesture_recognition import views


urlpatterns = [
    path('', views.index, name='index'),
    path('live_feed', views.live_feed, name='live_feed'),
]
