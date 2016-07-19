#coding: utf-8
from django.db import models
from django.core.urlresolvers import reverse_lazy

class Photo(models.Model):
    image_file = models.ImageField(upload_to='%Y/%m/%d')
    filtered_image_file = models.ImageField(upload_to='static_files/uploaded/%Y/%m/%d')
    description = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    def delete(self, *args, **kwargs):
        self.image_file.delete()
        self.filtered_image_file.delete()
        super(Photo,self).delete(*args, **kwargs)

    def get_absolute_url(self):
        return reverse_lazy('view_single_photo',kwargs={'photo_id':self.id})
