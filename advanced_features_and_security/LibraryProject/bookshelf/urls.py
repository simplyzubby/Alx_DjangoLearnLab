from django.urls import path
from .views import view_books, create_book, edit_book, delete_book

urlpatterns = [
    path("books/", view_books, name="view_books"),
    path("books/create/", create_book, name="create_book"),
    path("books/edit/<int:book_id>/", edit_book, name="edit_book"),
    path("books/delete/<int:book_id>/", delete_book, name="delete_book"),
]