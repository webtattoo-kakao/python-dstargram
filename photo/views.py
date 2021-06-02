from django.shortcuts import render

# Create your views here.
from .models import Photo





def photo_list(request):

    photo_data_list = Photo.objects.all()

    return render(request, 'photo/list.html', {
       'photo_data_list': photo_data_list
    })

