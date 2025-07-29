from rest_framework import serializers
from .models import Book, Comment


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title']


class CommentSerializer(serializers.ModelSerializer):
    book = BookSerializer()

    class Meta:
        model = Comment
        fields = ['id', 'text', 'book']
