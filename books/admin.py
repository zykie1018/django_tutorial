from django.contrib import admin
from books.models import Author, Book, Classification, Publisher


class AuthorAdmin(admin.ModelAdmin):
    fields = ['email', 'first_name', 'last_name']
    
    
class BookAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Details', {'fields': ['title', 'authors', 'publisher', 'classification']}),
        ('Date information', {
            'fields': ['publication_date'],
            'classes': ['collapse'],
        }),
    ]
    list_display = ['title', 'publisher', 'was_published_recently']
    list_filter = ['publication_date']
    search_fields = ['title']
    filter_horizontal = ['authors']
    

class ClassificationAdmin(admin.ModelAdmin):
    fields = ['code', 'name', 'description']

class BookInLine(admin.TabularInline):
    model = Book
    extra = 3


class PublisherAdmin(admin.ModelAdmin):
    inlines = [BookInLine]
    
    
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Classification, ClassificationAdmin)
