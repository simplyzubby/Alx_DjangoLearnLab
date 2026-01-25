from django.shortcuts import render, redirect
from django.contrib.auth.decorators import permission_required
from .models import Book

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