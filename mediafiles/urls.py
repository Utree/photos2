# coding: utf-8
from django.conf.urls import url
from django.urls import path
from mediafiles import views
urlpatterns = [
    path('api_v1/images/<image_path>/', views.index, name='index'),
]
