from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('shows/', views.shows_all, name='show_all'),
    path('shows/<int:id>/', views.shows_detail, name='show_detail'),
]


