from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('posts', views.posts, name='posts'),
    path('resume', views.resume, name='resume'),
    path('contact', views.contact, name='contact')
]
