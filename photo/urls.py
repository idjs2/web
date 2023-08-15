from django.urls import path
from . import views

urlpatterns = [
    path('', views.photo_list, name='photo_list'),  # http://127.0.0.1:8000/
    path('test', views.test, name='test'),  # http://127.0.0.1:8000/test
]