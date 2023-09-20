from django.db import models

class Gallery(models.Model):
    title = models.CharField(max_length=100)

class Image(models.Model):
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='gallery_images/')
