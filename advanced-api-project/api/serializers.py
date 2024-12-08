from rest_framework import serializers
from .models import Book , Author
from django.utils import timezone


class BookSerializer(serializers.ModelSerializer):
    # A book serializer for the book model it contains all the fields of the book model
    class Meta :
        model = Book
        fields = '__all__'
    
    def validate_publication_year(self, value):
        # Validation of publication year
        if value > timezone.now():
            raise serializers.ValidationError({'publication_year': 'Cannot be in the future'})

class AuthorSerializer(serializers.ModelSerializer):
    # Author serializer which the author model is related to the book model the serializer contains a field for the author
    book = BookSerializer()
    class Meta :
        model = Author
        fields = ['name', 'book']
