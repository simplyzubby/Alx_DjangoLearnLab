from django.apps import AppConfig
from django.db.models.signals import post_migrate


class BookshelfConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "bookshelf"

    def ready(self):
        post_migrate.connect(create_groups, sender=self)


def create_groups(sender, **kwargs):
    from django.contrib.auth.models import Group, Permission
    from django.contrib.contenttypes.models import ContentType
    from .models import Book

    book_ct = ContentType.objects.get_for_model(Book)

    # Custom permissions
    view_perm = Permission.objects.get(codename="can_view", content_type=book_ct)
    create_perm = Permission.objects.get(codename="can_create", content_type=book_ct)
    edit_perm = Permission.objects.get(codename="can_edit", content_type=book_ct)
    delete_perm = Permission.objects.get(codename="can_delete", content_type=book_ct)

    # Groups
    admin_group, _ = Group.objects.get_or_create(name="Admins")
    editor_group, _ = Group.objects.get_or_create(name="Editors")
    viewer_group, _ = Group.objects.get_or_create(name="Viewers")

    admin_group.permissions.set([view_perm, create_perm, edit_perm, delete_perm])
    editor_group.permissions.set([view_perm, create_perm, edit_perm])
    viewer_group.permissions.set([view_perm])

class BookshelfConfig(AppConfig):
    name = 'bookshelf'
