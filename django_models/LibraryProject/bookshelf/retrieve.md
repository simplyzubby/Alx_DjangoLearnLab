## 📄 `retrieve.md`

```md
# Retrieve Book

## Python Command
```python
book = Book.objects.get(title="1984")
book.id, book.title, book.author, book.publication_year
Output
(1, '1984', 'George Orwell', 1949)
Comment:
The book was retrieved successfully and all attributes were displayed.
