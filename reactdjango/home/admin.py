from django.contrib import admin

# Register your models here.
from .models import Book, Author


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'read', 'author')


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')


admin.site.register(Book, BookAdmin)

admin.site.register(Author, AuthorAdmin)