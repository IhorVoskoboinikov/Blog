from django.urls import path
from posts.api import PostsListAPIView, PostRetrieveAPIView

app_name = 'posts_api'

urlpatterns = [
    # APIs
    path("posts/", PostsListAPIView.as_view(), name='posts'),
    path("posts/<int:id>/", PostRetrieveAPIView.as_view(), name='post_detail'),

]