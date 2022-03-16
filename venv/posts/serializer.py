from django.contrib.auth import get_user_model
from rest_framework import serializers


from .models import Post

User = get_user_model()

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = ["id", "username", "email"] (Поля которые мы хоти, чтобы отображались в Ростмен.
        # Если мы хотим исключить поле в Постмен - "password"
        exclude = ["password"]
        # fields = "__all__" (Выводим всю инфо про автора)


class PostSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()

    class Meta:
        model = Post
        fields = ["id", "title", "content", "author"]






