from django.shortcuts import get_object_or_404, render, redirect

# Create your views here.
from .models import Photo

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

#@login_required
def photo_list(request):

    photo_data_list = Photo.objects.order_by('-created').all()

    return render(request, 'photo/list.html', {
       'photo_data_list': photo_data_list
    })


class PhotoUploadView(LoginRequiredMixin, CreateView):
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

class PhotoUpdateView(LoginRequiredMixin, UpdateView):
    model = Photo
    fields = ['photo', 'text']
    template_name_suffix = '_update'


class PhotoDeleteView(LoginRequiredMixin, DeleteView):
    model = Photo
    template_name = 'photo/photo_delete.html'
    success_url = '/'

class PhotoDetailView(DetailView):
    model = Photo
    
