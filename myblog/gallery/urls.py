from django.urls import path
from . import views

urlpatterns = [
    path('galleries/', views.gallery_list, name='gallery_list'),
    path('gallery/<int:gallery_id>/', views.image_list, name='image_list'),
    path('gallery/<int:gallery_id>/<int:image_id>/', views.image_detail, name='image_detail'),
]
