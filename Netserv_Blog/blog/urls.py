from django.urls import path, include 
from .views import Add_Post, view_events, view_posts, like_post

urlpatterns = [
    path('add_post', Add_Post, name='add_post'),
    path('', view_events, name='home'),
    path('posts', view_posts, name='posts'),
    path('events', view_events, name='events'),
    path('Announcements', view_events, name='announcements'),
    path('like', like_post, name='like'),
]
