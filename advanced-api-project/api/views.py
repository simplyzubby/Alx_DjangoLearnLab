from rest_framework import generics, permissions, filters
from rest_framework.response import Response
from rest_framework import status
from .models import Book
from .serializers import BookSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

# ------------------------------
# Book API Views
# ------------------------------
class BookListView(generics.ListAPIView):
    """
    List all books with advanced query capabilities:
    
    1. Filtering: Filter by 'title', 'author', and 'publication_year'
       Example: /api/books/?publication_year=2006
    2. Search: Perform text search on 'title' or 'author__name'
       Example: /api/books/?search=Half
    3. Ordering: Order results by 'title' or 'publication_year'
       Example: /api/books/?ordering=publication_year
       Use '-ordering_field' for descending order
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    # Filter by these fields
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['title', 'author', 'publication_year']  # exact match filtering
    search_fields = ['title', 'author__name']  # text search
    ordering_fields = ['title', 'publication_year']  # fields allowed for ordering
    ordering = ['title']  # default ordering


class BookDetailView(generics.RetrieveAPIView):
    """
    Retrieve a single book by ID.
    GET /api/books/<id>/
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

class BookCreateView(generics.CreateAPIView):
    """
    Create a new book.
    - Validates publication_year (handled by serializer)
    - Only authenticated users can create a book
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated] # Only logged-in users can create

    def perform_create(self, serializer):
        """
        Additional customization on save.
        You could add logic here such as associating the book with the request user.
        """
        serializer.save()


class BookUpdateView(generics.UpdateAPIView):
    """
    Update an existing book by ID.
    - Partial updates allowed (PATCH)
    - Validates data using the serializer
    - Only authenticated users can update
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Only logged-in users can update

    def perform_update(self, serializer):
        """
        Custom logic during update.
        Example: log changes, check conditions, or apply filters
        """
        serializer.save()



class BookDeleteView(generics.DestroyAPIView):
    """
    Delete a book by ID.
    DELETE /api/books/<id>/
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]