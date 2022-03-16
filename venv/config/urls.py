# import .....
from django.contrib import admin
from django.urls import path, include
# from posts.views import PostsListView, PostDetailView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.http import HttpResponseRedirect

def redirect_to_posts(request):
    return HttpResponseRedirect("posts/")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", redirect_to_posts),
    path("posts/", include('posts.urls')),
    path("accounts/", include('django.contrib.auth.urls')),
    path("accounts/", include('accounts.urls')),


    path("api/", include('posts.api_urls')),

    # path("authentication/", include('authentication.urls')),
    # path("another_app/", include('another_app.urls')),

]


urlpatterns += staticfiles_urlpatterns()