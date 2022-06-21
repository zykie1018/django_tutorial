from xml.dom import ValidationErr
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth import authenticate, login

from books.models import Book, Author
from .forms import AuthorForm, ContactForm


def index(request):
        book_list = Book.objects.all()
        # output = [book for book in book_list]
            
        
        return render(request,
                    'books/book_list.html',
                    {'book_list': book_list},
        )


# def search_form(request):
#         return render(request,
#                       'books/search_form.html')
        
        
def search(request):
    error = False
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            error = True
        else:
            books = Book.objects.filter(title__icontains=q)
            return render(
                request,
                'books/search_results.html',
                {'books': books, 'query': q},
            )
    return render(request, 'books/search_form.html', {'error': error})


def contact(request):
    if request.method == 'POST':  # If the form has been submitted...
        form = ContactForm(request.POST)  # A form bound to the POST data
        if form.is_valid():  # All validation rules pass
            
            # Process the data in form.cleaned_data
            # ...
            return HttpResponseRedirect('/thanks/')
    else:
        form = ContactForm()  # An unbound form

    return render(
        request,
        'books/contact.html',
        {'form': form}
    )
    

def detail(request, id):
    book_detail = Book.objects.get(id=id)
    return render(request,
                'books/book_detail.html',
                {'book_detail': book_detail}
    )
  
  
def author_details(request, author_id):
    book_detail = Book.objects.filter(authors=author_id)
    author_detail = Author.objects.get(id=author_id)
    return render(request,
                  'books/author_details.html',
                  {'book_detail': book_detail, 'author_detail': author_detail}
    )
    
   
        
def add_author(request):
    form = AuthorForm()
    new_author = []
    if request.method == 'POST':
        form = AuthorForm(request.POST)
            
        if form.is_valid():
            # add code here
            new_author = form.save()
            form = AuthorForm()
            return HttpResponseRedirect('/thanks/')
    
    return render(request,
                  'books/author.html',
                  {'form': form, 'new_author': new_author}
    )


# def redirect_url(request):
#     url = reverse(<app> 'url')
#     return HttpResponseRedirect()


def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    
    if user is not None:
        if user.is_active:
            login(request, user)
            
            return render(request,
                          'books/login_success.html',
                          {'username': username}
            )
        else:
            pass
        
    else:
        pass
    

def logout_view(request):
    return HttpResponseRedirect()