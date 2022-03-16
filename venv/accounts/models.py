"""
Post:
id: int
title: str
content: str
author_id: int

User:
id: int
username: str
first_name: str
last_name: str
password: str
"""

from django.conf import settings
from django.db import models


# class User (models.Model): #Импортировали из Django =>from django.contrib.auth.models import User стр = 16
#     #id = defout interger
#
#     user_name = models.CharField(max_length=255)
#     first_name = models.CharField(max_length=255)
#     last_name = models.CharField(max_length=255)
#     password = models.CharField(max_length=255)

class Post (models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="accounts", on_delete=models.CASCADE)

    #If we don`t wanna use real delete from database. Look into the view.py PostsListView
    # deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    # def save(self):
    #     self.author_id = 1
    #     return super().save()

# User.objects.get (id=3)
# me.posts.all()<== Queryset()

# Менеджер в Django!!!!
# Post.object.all() <== Queryset()
# Post.object.first() <== Model
# Post.object.last()
# Post.object.create()
# Post.object.update()
# post = Post.objects.get (author_id=3)
# result = Post.object.filter (title = "VIM")
# Что такое result ?
# result -> Qweryset () -> dict (Qweryset - имеет болеше словарь)
# post = Post.object.first()

#results = [{}, {}, {}]
# post = results [2]

# post = {
#     "id": 1,
#     "title": "VIM"
#     "content": "How to learn VIM"
#     "author_id": 3
# }

# post("title") = > post id /post.content
#==========================
# post = Post.objects.get (title = "VIM")
# ????? post.author.username ????
# author = User.objects.get (id = post.author_id)
# author_username !!!!!



