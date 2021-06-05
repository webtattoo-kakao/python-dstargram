from django.shortcuts import render, redirect

# Create your views here.
from .models import Photo

from django.views.generic.edit import CreateView


def photo_list(request):

    photo_data_list = Photo.objects.order_by('-created').all()

    return render(request, 'photo/list.html', {
       'photo_data_list': photo_data_list
    })


# GET, POST
class PhotoUploadView(CreateView):
    model = Photo
    fields = [
        'photo', 'text'
    ]
    template_name = 'photo/upload.html'

    def form_valid(self, form):
        form.instance.author_id = self.request.user.id

        if not form.is_valid():
            return self.render_to_response({
                'form': form
            })

        form.instance.save()
        return redirect('/')


        """
        if form.is_valid():
            form.instance.save()
            return redirect('/')
        else:
            return self.render_to_response({
                'form': form
            })
        """