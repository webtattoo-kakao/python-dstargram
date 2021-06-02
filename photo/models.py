from django.db import models

from django.contrib.auth.models import User

# Create your models here.


class Photo(models.Model):

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_photos', verbose_name='작성자')

    photo = models.ImageField(upload_to='photo/%Y/%m/%d', default='photo/no_image.png')
    text = models.TextField()

    created = models.DateTimeField(auto_now_add=True, verbose_name='작성일')
    updated = models.DateTimeField(auto_now=True, verbose_name='수정일')


    def __str__(self):
        return self.author.first_name + ',' + self.author.last_name + " - " + self.created.strftime('%Y-%m-%d %H:%M:%S')