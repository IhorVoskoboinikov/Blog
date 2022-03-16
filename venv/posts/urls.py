from django.urls import path

from posts.views import (PostsListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView)





#We use this namespaces in urls in templates

app_name = 'posts'

urlpatterns = [
    path("", PostsListView.as_view(), name='list'),
    path("<int:pk>/", PostDetailView.as_view(), name='detail'),
    path("new/", PostCreateView.as_view(), name='create'),
    path("update/<int:pk>/", PostUpdateView.as_view(), name='update'),
    path("delete/<int:pk>/", PostDeleteView.as_view(), name='delete'),


]