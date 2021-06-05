from django.shortcuts import render

# Create your views here.
from .models import Photo

from django.views.generic.edit import CreateView


def photo_list(request):

    photo_data_list = Photo.objects.all()

    return render(request, 'photo/list.html', {
       'photo_data_list': photo_data_list
    })


class PhotoUploadView(CreateView):
    model = Photo
    fields = [
        'photo', 'text'
    ]
    template_name = 'photo/upload.html'