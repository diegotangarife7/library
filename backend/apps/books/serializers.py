from rest_framework import serializers

from .models import Book

from apps.author.serializers import AuthorSerializer



class BookSerializer(serializers.ModelSerializer):

    author = AuthorSerializer()
    
    class Meta:
        model = Book
        fields = [
            'id',
            'title',
            'author',
            'year_edition',
            'number_pages',
            'language',
            'editorial',
        ]

    def validate_number_pages(self, value):
        if value <= 0:
            raise serializers.ValidationError('El numero de paginas debe ser mayor a cero')
        return value
