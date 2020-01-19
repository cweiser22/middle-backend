from rest_framework import serializers
from djoser.serializers import UserSerializer
from .models import *


class ArticleSerializer(serializers.ModelSerializer):
    author = UserSerializer(many=False, read_only=True)

    class Meta:
        model = Article
        fields = ('id', 'title', 'description', 'content', 'created_at', 'author', 'category')

