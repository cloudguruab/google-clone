from django.urls import path 
from . import views

urlpatterns = [
    path('', views.index, name='indexs'),
    path('search', views.search, name='search')
]