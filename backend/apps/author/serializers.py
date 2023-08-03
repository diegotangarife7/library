from rest_framework import serializers

from .models import Author



class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = [
            'id',
            'name',
            'country',
            'age'
        ]

    def validate_age(self, value):
        if value <= 0:
            raise serializers.ValidationError('la edad debe ser mayor a cero')
        return value


class ListAuthorSerializer(serializers.ModelSerializer):

    country = serializers.SerializerMethodField()

    class Meta:
        model = Author
        fields = [
            'id',
            'name',
            'country',
            'age'
        ]

    def get_country(self, obj):
        return obj.get_country_display()