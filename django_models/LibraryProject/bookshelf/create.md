# Create Book

## Python Command
```python
from bookshelf.models import Book

book = Book.objects.create(
    title="1984",
    author="George Orwell",
    publication_year=1949
)

book

Output
<Book: 1984>

Comment:
The Book instance was successfully created and stored in the database.
