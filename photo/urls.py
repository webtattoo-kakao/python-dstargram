
from django.contrib import admin
from django.urls import path

from . import views
from .views import PhotoUploadView

app_name = 'photo'

urlpatterns = [
    path('', views.photo_list, name='photo_list'),
    path('upload/', PhotoUploadView.as_view(), name='photo_upload'),
]
