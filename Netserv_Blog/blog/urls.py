from django.urls import path, include 
from .views import Add_Post, view_events, my_view_posts, like_post, post_details, post_delete, annoucement


urlpatterns = [
    path('add_post', Add_Post, name='add_post'),
    path('', view_events, name='home'),
    path('posts', my_view_posts, name='posts'),
    path('events', view_events, name='events'),
    path('annoucement', annoucement, name='announcements'),
    path('like', like_post, name='like'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', post_details, name='post_details'),
    path('delete', post_delete, name='post_delete'),
]
