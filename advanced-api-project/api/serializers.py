from rest_framework import serializers
from datetime import datetime
from .models import Author, Book


class BookSerializer(serializers.ModelSerializer):
    """
    BookSerializer

    Purpose:
    - Converts Book model instances into JSON format.
    - Validates incoming data before saving to the database.

    Features:
    - Serializes all fields of the Book model.
    - Implements custom validation to prevent future publication years.
    """

    class Meta:
        model = Book
        fields = '__all__'

    def validate_publication_year(self, value):
        """
        Custom field-level validation.

        Ensures that the publication year is not greater
        than the current year.
        """
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError(
                "Publication year cannot be in the future."
            )
        return value


class AuthorSerializer(serializers.ModelSerializer):
    """
    AuthorSerializer

    Purpose:
    - Serializes Author instances.
    - Dynamically includes related Book objects using nested serialization.

    Relationship Handling:
    - Uses the 'books' related_name defined in the Book model.
    - Nested BookSerializer allows one-to-many representation.
    """

    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']