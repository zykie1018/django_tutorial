from xml.dom import ValidationErr
from django.conf import settings
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import TemplateView, View

from books.models import Book, Author, Classification, Publisher
from books.forms import (
    AuthorForm,
    ContactForm,
    BookForm,
    PublisherForm,
    AuthorUpdateForm,
    BookUpdateForm,
    PublisherUpdateForm,
    AuthorDeleteForm,
    BookDeleteForm,
    PublisherDeleteForm,
    LoginForm,
    RegisterForm,
)


class AboutView(TemplateView):
    template_name = "books/about.html"


""" ADDING OF AUTHORS, BOOKS, PUBLISHERS """


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
            form.save()
            messages.success(request, "Successfully Added Author")
            return HttpResponseRedirect(reverse("books:new-form"))

        return render(request, self.template_name, {"form": form})


class BookAddView(View):
    form_class = BookForm
    initial = {"key": "value"}
    template_name = "books/book_add.html"

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # Clean data here
            form.save()
            messages.success(request, "Successfully Added Book")
            return HttpResponseRedirect(reverse("books:add-book-form"))

        return render(request, self.template_name, {"form": form})


class PublisherAddView(View):
    form_class = PublisherForm
    initial = {"key": "value"}
    template_name = "books/publisher_add.html"

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # Clean data here
            form.save()
            messages.success(request, "Successfully Added Publisher")
            return HttpResponseRedirect(reverse("books:add-publisher-form"))

        return render(request, self.template_name, {"form": form})


""" 
UPDATING OF AUTHORS, BOOKS, PUBLISHERS 
To populate fields use instance= as 2nd argument when initializing a form
get the .id of whichever model instance used
"""


class AuthorUpdateView(View):
    form_class = AuthorUpdateForm
    initial = {"key": "value"}
    template_name = "books/author_update.html"

    def get(self, request, pk, *args, **kwargs):
        author_update = Author.objects.get(pk=pk)
        form = self.form_class(initial=self.initial, instance=author_update)
        return render(request, self.template_name, {"form": form})

    def post(self, request, pk, *args, **kwargs):
        author_update = Author.objects.get(pk=pk)
        form = self.form_class(request.POST, instance=author_update)
        if form.is_valid():
            # Clean data here
            form.save()
            messages.success(request, "Successfully Updated Author")
            return redirect("books:update-author-form", author_update.id)

        return render(request, self.template_name, {"form": form})


class BookUpdateView(View):
    form_class = BookUpdateForm
    initial = {"key": "value"}
    template_name = "books/book_update.html"

    def get(self, request, pk, *args, **kwargs):
        book_update = Book.objects.get(pk=pk)
        form = self.form_class(initial=self.initial, instance=book_update)
        return render(request, self.template_name, {"form": form})

    def post(self, request, pk, *args, **kwargs):
        book_update = Book.objects.get(pk=pk)
        form = self.form_class(request.POST, instance=book_update)
        if form.is_valid():
            # Clean data here
            form.save()
            messages.success(request, "Successfully Updated Book")
            return redirect("books:update-book-form", book_update.id)

        return render(request, self.template_name, {"form": form})


class PublisherUpdateView(View):
    form_class = PublisherUpdateForm
    initial = {"key": "value"}
    template_name = "books/publisher_update.html"

    def get(self, request, pk, *args, **kwargs):
        publisher_update = Publisher.objects.get(pk=pk)
        form = self.form_class(initial=self.initial, instance=publisher_update)
        return render(request, self.template_name, {"form": form})

    def post(self, request, pk, *args, **kwargs):
        publisher_update = Publisher.objects.get(pk=pk)
        form = self.form_class(request.POST, instance=publisher_update)
        if form.is_valid():
            # Clean data here
            form.save()
            messages.success(request, "Successfully Updated Publisher")
            return redirect("books:update-publisher-form", publisher_update.id)

        return render(request, self.template_name, {"form": form})


""" 
DELETION OF AUTHORS, BOOKS, PUBLISHERS 
To populate fields use instance= as 2nd argument when initializing a form
get the .id of whichever model instance used
"""


class AuthorDeleteView(View):
    form_class = AuthorDeleteForm
    initial = {"key": "value"}
    template_name = "books/author_delete.html"

    def get(self, request, pk, *args, **kwargs):
        author_delete = Author.objects.get(pk=pk)
        form = self.form_class(initial=self.initial, instance=author_delete)
        return render(request, self.template_name, {"form": form})

    def post(self, request, pk, *args, **kwargs):
        author_delete = Author.objects.get(pk=pk)
        form = self.form_class(request.POST, instance=author_delete)
        if form.is_valid():
            # Clean data here
            author_delete.delete()
            messages.success(request, "Successfully Deleted Author")
            return redirect("books:new-form")

        return render(request, self.template_name, {"form": form})


class BookDeleteView(View):
    form_class = BookDeleteForm
    initial = {"key": "value"}
    template_name = "books/book_delete.html"

    def get(self, request, pk, *args, **kwargs):
        book_delete = Book.objects.get(pk=pk)
        form = self.form_class(initial=self.initial, instance=book_delete)
        return render(request, self.template_name, {"form": form})

    def post(self, request, pk, *args, **kwargs):
        book_delete = Book.objects.get(pk=pk)
        form = self.form_class(request.POST, instance=book_delete)
        if form.is_valid():
            # Clean data here
            book_delete.delete()
            messages.success(request, "Successfully Deleted Book")
            return redirect("books:add-book-form")

        return render(request, self.template_name, {"form": form})


class PublisherDeleteView(View):
    form_class = PublisherDeleteForm
    initial = {"key": "value"}
    template_name = "books/publisher_delete.html"

    def get(self, request, pk, *args, **kwargs):
        pub_delete = Publisher.objects.get(pk=pk)
        form = self.form_class(initial=self.initial, instance=pub_delete)
        return render(request, self.template_name, {"form": form})

    def post(self, request, pk, *args, **kwargs):
        pub_delete = Publisher.objects.get(pk=pk)
        form = self.form_class(request.POST, instance=pub_delete)
        if form.is_valid():
            # Clean data here
            pub_delete.delete()
            messages.success(request, "Successfully Deleted Publisher")
            return redirect("books:add-publisher-form")

        return render(request, self.template_name, {"form": form})


@login_required(login_url="books:login")
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


@login_required(login_url="books:login")
def detail(request, pk):
    try:
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        raise Http404()
    return render(request, "books/book_detail.html", {"book": book})


# def add_author(request):
#     form = AuthorForm()
#     new_author = []
#     if request.method == "POST":
#         form = AuthorForm(request.POST)

#         if form.is_valid():
#             # add code here
#             new_author = form.save()
#             return redirect(reverse("books:new-form"))

#     return render(
#         request, "books/author.html", {"form": form, "new_author": new_author}
#     )


@login_required(login_url="books:login")
def author_details(request, author_id):
    book_detail = Book.objects.filter(authors=author_id)
    author_detail = Author.objects.get(id=author_id)
    return render(
        request,
        "books/author_details.html",
        {"book_detail": book_detail, "author_detail": author_detail},
    )


@login_required(login_url="books:login")
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
            return HttpResponseRedirect(reverse("books:new-contact"))
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


def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if form.is_valid():
            if user is not None:
                if user.is_active:
                    login(request, user)

                    return render(
                        request, "books/login_page.html", {"username": username}
                    )
                else:
                    return HttpResponse("The username and password were incorrect")

    else:
        form = LoginForm()

    return render(request, "books/login.html", {"form": form})


def user_register(request):
    form = RegisterForm
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            # login(request, user)
            messages.success(request, "Successfully Registered")
            return redirect("books:register")
        else:
            return redirect("books:register")
    return render(request, "books/register.html", {"form": form})


def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse("books:login"))


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


def search_author(request):
    error = False
    if "query" in request.GET:
        query = request.GET["query"]
        if not query:
            error = True
        else:
            authors = Author.objects.filter(first_name__icontains=query)
            return render(
                request,
                "books/search_author_results.html",
                {"authors": authors, "query": query},
            )
    return render(
        request,
        "books/search_author.html",
        {"error": error},
    )


def search_publisher(request):
    error = False
    if "query" in request.GET:
        query = request.GET["query"]
        if not query:
            error = True
        else:
            publishers = Publisher.objects.filter(name__icontains=query)
            return render(
                request,
                "books/search_publishers_results.html",
                {"publishers": publishers, "query": query},
            )
    return render(
        request,
        "books/search_publishers.html",
        {"error": error},
    )


def display_meta(request):
    values = request.META.items()
    values.sort()
    html = []
    for k, v in values:
        html.append(f"<tr><td>{k}</td><td>{v}</td></tr>")
    return HttpResponse(f"Welcome to the page at {request.path}")
