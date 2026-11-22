from django.contrib import admin
from ..models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "category", "total_copies", "available_copies")
    list_filter = ("category",)
    search_fields = ("title", "author", "isbn")
