from django.urls import path
from django.views.generic import TemplateView
from books.views import (
    AboutView,
    AuthorUpdateView,
    AuthorDeleteView,
    MyFormView,
    BookAddView,
    BookUpdateView,
    BookDeleteView,
    PublisherAddView,
    PublisherUpdateView,
    PublisherDeleteView,
)

# from . import views
from books import views

app_name = "books"
urlpatterns = [
    path("", views.index, name="index"),
    path("author/", MyFormView.as_view(), name="new-form"),
    path(
        "author/update/<int:pk>", AuthorUpdateView.as_view(), name="update-author-form"
    ),
    path(
        "author/delete/<int:pk>", AuthorDeleteView.as_view(), name="delete-author-form"
    ),
    path("add-book/", BookAddView.as_view(), name="add-book-form"),
    path("add-book/update/<int:pk>", BookUpdateView.as_view(), name="update-book-form"),
    path("add-book/delete/<int:pk>", BookDeleteView.as_view(), name="delete-book-form"),
    path("add-publisher/", PublisherAddView.as_view(), name="add-publisher-form"),
    path(
        "add-publisher/update/<int:pk>",
        PublisherUpdateView.as_view(),
        name="update-publisher-form",
    ),
    path(
        "add-publisher/delete/<int:pk>",
        PublisherDeleteView.as_view(),
        name="add-publisher-form",
    ),
    path("contact/", views.contact, name="new-contact"),
    path(
        "classification/",
        views.classify_books,
        name="classification-details",
    ),
    path(
        "classification/display/",
        views.display_classify_books,
        name="classification-display",
    ),
    path("details/<int:pk>", views.detail, name="book-details"),
    path("details/author/<int:author_id>", views.author_details, name="author-details"),
    path("search/", views.search),
    path("search/author", views.search_author, name="search-author"),
    path("search/publisher", views.search_publisher, name="search-publisher"),
    path("about/", AboutView.as_view()),
    path("login/", views.user_login, name="login"),
    path("logout/", views.user_logout, name="logout"),
    path("register/", views.user_register, name="register"),
]
