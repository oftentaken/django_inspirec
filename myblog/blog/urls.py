from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<slug:slug>/', views.page_detail, name='page_detail'),
    path('article/<slug:slug>/', views.article_detail, name='article_detail'),
    path('real-estate/<slug:slug>/', views.real_estate_page_detail, name='real_estate_page_detail'),
]
