from rest_framework import serializers
from book.models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'title', 'author', 'price', 'content', 'status')
        model = Book