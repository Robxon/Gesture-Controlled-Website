from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
import gesture_recognition

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('gesture_recognition.urls'))
]

urlpatterns += staticfiles_urlpatterns()