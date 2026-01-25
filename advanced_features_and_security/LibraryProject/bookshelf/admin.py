from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Book
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser

    # Fields shown in the user list page
    list_display = (
        'username',
        'email',
        'date_of_birth',
        'is_staff',
        'is_active',
    )

    # Fields that can be searched
    search_fields = ('username', 'email')

    # Filters in the right sidebar
    list_filter = ('is_staff', 'is_active')

    # Field layout when viewing/editing a user
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Information', {
            'fields': ('date_of_birth', 'profile_photo'),
        }),
    )

    # Field layout when creating a user
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Additional Information', {
            'fields': ('date_of_birth', 'profile_photo'),
        }),
    )

admin.site.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "publication_year")
    list_filter = ("publication_year", "author")
    search_fields = ("title", "author")
