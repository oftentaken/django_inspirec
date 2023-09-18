from django.shortcuts import render, get_object_or_404
from .models import Gallery, Image

def gallery_list(request):
    galleries = Gallery.objects.all()
    return render(request, 'gallery_list.html', {'galleries': galleries})

def image_list(request, gallery_id):
    gallery = get_object_or_404(Gallery, pk=gallery_id)
    images = Image.objects.filter(gallery=gallery)
    return render(request, 'image_list.html', {'gallery': gallery, 'images': images})

def image_detail(request, gallery_id, image_id):
    image = get_object_or_404(Image, pk=image_id)
    return render(request, 'image_detail.html', {'image': image})
