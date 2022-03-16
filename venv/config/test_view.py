from django.http import HttpResponse
from django.urls import path
from .test_view import foo

def foo (r) -> HttpResponse:
    return HttpResponse ("Hello")


urlpatterns = [
    path('foo/', admin.site.urls),
    path('foo/', foo),
]