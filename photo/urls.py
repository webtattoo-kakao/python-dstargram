
from django.contrib import admin
from django.urls import path

from . import views
from .views import PhotoUploadView
from .views import PhotoUpdateView
from .views import PhotoDetailView
from .views import PhotoDeleteView

app_name = 'photo'

urlpatterns = [
    path('', views.photo_list, name='photo_list'),    
    path('upload/', PhotoUploadView.as_view(), name='photo_upload'),
    path('detail/<int:pk>', PhotoDetailView.as_view(), name='photo_detail'),
    path('update/<int:pk>', PhotoUpdateView.as_view(), name='photo_update'),
    path('delete/<int:pk>', PhotoDeleteView.as_view(), name='photo_delete'),
]
