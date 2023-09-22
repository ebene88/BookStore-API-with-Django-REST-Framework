from rest_framework import serializers
from book.models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('category', 'id', 'title', 'pdf', 'image', 
                  'slug','author', 'price', 'content', 'status')
        model = Book