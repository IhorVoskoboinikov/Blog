from django.http import JsonResponse
from .serializer import PostSerializer

from .models import Post

from rest_framework.generics import ListAPIView, RetrieveAPIView
# from rest_framework.response import Response

# def _get_posts_data() -> list:
#     posts = Post.objects.all()
#     posts_data = []
#
#     for post in posts:
#         posts_data.append({
#             "id": post.id,
#             "title": post.title,
#             "author": {
#                 "id": post.author.id,
#                 "username": post.author.username,
#             },
#
#         })
#     return posts_data

class PostsListAPIView(ListAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

# def posts(request):
#     posts = Post.objects.all()
#     serializer = PostSerializer(posts, many=True)
#
#
#     return JsonResponse({"results": serializer.data})

# class AuthorSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         # fields = ["id", "username", "email"] (Поля которые мы хоти, чтобы отображались в Ростмен.
#         # Если мы хотим исключить поле в Постмен - "password"
#         exclude = ["password"]
#         # fields = "__all__" (Выводим всю инфо про автора)
#
#
# class PostSerializer(serializers.ModelSerializer):
#     author = AuthorSerializer()
#
#     class Meta:
#         model = Post
#         fields = ["id", "title", "content", "author"]

class PostRetrieveAPIView(RetrieveAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    lookup_field = "id"



