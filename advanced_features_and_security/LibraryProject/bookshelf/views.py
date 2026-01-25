from turtle import title
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import permission_required
from .models import Book
from django.shortcuts import render
from .forms import SearchForm
from .forms import BookForm
from django.db import connection

with connection.cursor() as cursor:
    cursor.execute(
        "SELECT * FROM bookshelf_book WHERE title = %s",
        [title]
    )

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = BookForm()

    return render(request, 'bookshelf/form.html', {'form': form})

def search_books(request):
    form = SearchForm(request.GET)
    books = Book.objects.none()

    if form.is_valid():
        query = form.cleaned_data['q']
        books = Book.objects.filter(title__icontains=query)

    return render(request, 'bookshelf/results.html', {
        'form': form,
        'books': books
    })

@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, "bookshelf/book_list.html", {"books": books})


@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    if request.method == "POST":
        title = request.POST.get("title")
        author = request.POST.get("author")
        publication_year = request.POST.get("publication_year")

        Book.objects.create(
            title=title,
            author=author,
            publication_year=publication_year
        )
        return redirect("view_books")

    return render(request, "bookshelf/create_book.html")

@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, book_id):
    book = Book.objects.get(id=book_id)

    if request.method == "POST":
        book.title = request.POST.get("title")
        book.author = request.POST.get("author")
        book.publication_year = request.POST.get("publication_year")
        book.save()
        return redirect("view_books")

    return render(request, "bookshelf/edit_book.html", {"book": book})

@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, book_id):
    book = Book.objects.get(id=book_id)

    if request.method == "POST":
        book.delete()
        return redirect("view_books")

    return render(request, "bookshelf/delete_book.html", {"book": book})