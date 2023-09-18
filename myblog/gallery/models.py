from django.db import models

class Gallery(models.Model):
    title = models.CharField(max_length=100)

    class Meta:
        app_label = 'gallery'  # Add this line to specify the app label

class Image(models.Model):
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='gallery_images/')
