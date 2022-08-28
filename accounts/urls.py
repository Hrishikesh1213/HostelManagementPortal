from django.urls import path
from . import views

urlpatterns = [
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('myprofile', views.myprofile, name='myprofile'),
    path('editprofile', views.editprofile, name='editprofile')
]
