## 📄 `CRUD_operations.md`

```md
# CRUD Operations Using Django ORM

This document demonstrates Create, Retrieve, Update, and Delete (CRUD)
operations performed on the Book model using the Django shell.

---

## Create
```python
Book.objects.create(
    title="1984",
    author="George Orwell",
    publication_year=1949
)
Retrieve
Book.objects.get(title="1984")
Update
book.title = "Nineteen Eighty-Four"
book.save()
Delete
book.delete()
Book.objects.all()
