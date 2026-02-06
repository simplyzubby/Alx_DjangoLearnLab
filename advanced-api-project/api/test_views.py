from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from .models import Author, Book

class BookAPITestCase(APITestCase):
    """
    Test suite for Book API endpoints.
    Tests CRUD operations, filtering, searching, ordering, and permissions.
    """

    def setUp(self):
        """
        Set up initial data and test users.
        """
        # Create a test user
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.client = APIClient()

        # Create authors
        self.author1 = Author.objects.create(name="Chimamanda Ngozi Adichie")
        self.author2 = Author.objects.create(name="Ngugi wa Thiong'o")

        # Create books
        self.book1 = Book.objects.create(title="Half of a Yellow Sun", publication_year=2006, author=self.author1)
        self.book2 = Book.objects.create(title="Purple Hibiscus", publication_year=2003, author=self.author1)
        self.book3 = Book.objects.create(title="Wizard of the Crow", publication_year=2006, author=self.author2)

    # ----------------------------
    # Test: List Books
    # ----------------------------
    def test_list_books(self):
        url = reverse('book-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)

    # ----------------------------
    # Test: Retrieve a Book
    # ----------------------------
    def test_retrieve_book(self):
        url = reverse('book-detail', args=[self.book1.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.book1.title)

    # ----------------------------
    # Test: Create Book
    # ----------------------------
    def test_create_book_authenticated(self):
        self.client.login(username='testuser', password='testpass')
        url = reverse('book-create')
        data = {
            'title': 'Americanah',
            'publication_year': 2013,
            'author': self.author1.id
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 4)
        self.assertEqual(Book.objects.get(id=response.data['id']).title, 'Americanah')

    def test_create_book_unauthenticated(self):
        url = reverse('book-create')
        data = {
            'title': 'Americanah',
            'publication_year': 2013,
            'author': self.author1.id
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    # ----------------------------
    # Test: Update Book
    # ----------------------------
    def test_update_book_authenticated(self):
        self.client.login(username='testuser', password='testpass')
        url = reverse('book-update', args=[self.book1.id])
        data = {'title': 'Half of a Yellow Sun (Updated)'}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, 'Half of a Yellow Sun (Updated)')

    def test_update_book_unauthenticated(self):
        url = reverse('book-update', args=[self.book1.id])
        data = {'title': 'HYS Unauth Update'}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    # ----------------------------
    # Test: Delete Book
    # ----------------------------
    def test_delete_book_authenticated(self):
        self.client.login(username='testuser', password='testpass')
        url = reverse('book-delete', args=[self.book1.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(id=self.book1.id).exists())

    def test_delete_book_unauthenticated(self):
        url = reverse('book-delete', args=[self.book1.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    # ----------------------------
    # Test: Filtering
    # ----------------------------
    def test_filter_books_by_publication_year(self):
        url = reverse('book-list') + '?publication_year=2006'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  # book1 and book3

    # ----------------------------
    # Test: Searching
    # ----------------------------
    def test_search_books_by_title(self):
        url = reverse('book-list') + '?search=Purple'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Purple Hibiscus')

    # ----------------------------
    # Test: Ordering
    # ----------------------------
    def test_order_books_by_title_descending(self):
        url = reverse('book-list') + '?ordering=-title'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        titles = [book['title'] for book in response.data]
        self.assertEqual(titles, sorted(titles, reverse=True))

