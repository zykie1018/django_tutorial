from django.shortcuts import render

from .models import Book


def index(request):
        book_list = Book.objects.all()
        output = [book for book in book_list]
            
        
        return render(request,
                    'books/book_list.html',
                    {"output": output})
