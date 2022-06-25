from xml.dom import ValidationErr
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login
from django.views.generic import TemplateView, View

from books.models import Book, Author, Classification
from books.forms import AuthorForm, ContactForm


class AboutView(TemplateView):
    template_name = "books/about.html"


class MyFormView(View):
    form_class = AuthorForm
    initial = {"key": "value"}
    template_name = "books/author.html"

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # Clean data here
            return HttpResponseRedirect(reverse("books:new-form"))

        return render(request, self.template_name, {"form": form})


def index(request):
    book_list = Book.objects.all()
    # output = [book for book in book_list]
    response = ""

    if not book_list:
        response = "No books are available."

    return render(
        request,
        "books/book_list.html",
        {"book_list": book_list, "response": response},
    )


# def search_form(request):
#         return render(request,
#                       'books/search_form.html')


def detail(request, pk):
    try:
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        raise Http404()

    return render(request, "books/book_detail.html", {"book": book})


def add_author(request):
    form = AuthorForm()
    new_author = []
    if request.method == "POST":
        form = AuthorForm(request.POST)

        if form.is_valid():
            # add code here
            new_author = form.save()
            return redirect(reverse("books:new-form"))

    return render(
        request, "books/author.html", {"form": form, "new_author": new_author}
    )


def author_details(request, author_id):
    book_detail = Book.objects.filter(authors=author_id)
    author_detail = Author.objects.get(id=author_id)
    return render(
        request,
        "books/author_details.html",
        {"book_detail": book_detail, "author_detail": author_detail},
    )


def classify_books(request):
    classify_list = Classification.objects.all()
    return render(
        request, "books/classification.html", {"classify_list": classify_list}
    )


def contact(request):
    if request.method == "POST":  # If the form has been submitted...
        form = ContactForm(request.POST)  # A form bound to the POST data
        if form.is_valid():  # All validation rules pass

            # Process the data in form.cleaned_data
            # ...
            return HttpResponseRedirect("/thanks/")
    else:
        form = ContactForm()  # An unbound form

    return render(request, "books/contact.html", {"form": form})


# def get_detail(request, id):
#     book_detail = Book.objects.get(classification=id)
#     return render(request,
#                 'books/book_detail.html',
#                 {'book_detail': book_detail}
#     )


def display_classify_books(request):
    classify_books = Classification.objects.all()
    return render(
        request, "books/classification_display.html", {"classify_books": classify_books}
    )


def login(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(username=username, password=password)

    if user is not None:
        if user.is_active:
            login(request, user)

            return render(request, "books/login_success.html", {"username": username})
        else:
            pass

    else:
        pass


def logout_view(request):
    return HttpResponseRedirect()


def search(request):
    error = False
    if "q" in request.GET:
        q = request.GET["q"]
        if not q:
            error = True
        else:
            books = Book.objects.filter(title__icontains=q)
            return render(
                request,
                "books/search_results.html",
                {"books": books, "query": q},
            )
    return render(request, "books/search_form.html", {"error": error})
