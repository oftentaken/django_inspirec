from django.urls import path
from . import views

urlpatterns = [
    path('multiupload/', include('multiupload.urls', namespace='multiupload')),
]
