from django.urls import path, include 
from .views import Register, Login, Logout, EditProfile

urlpatterns = [
    path('register', Register, name='register'),
    path('login', Login, name='login'),
    path('logout', Logout, name='logout'),
    path('editProfile', EditProfile, name='editProfile'),
]
