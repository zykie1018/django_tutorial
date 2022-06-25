from django.urls import path
from django.views.generic import TemplateView
from books.views import AboutView, MyFormView

# from . import views
from books import views

app_name = "books"
urlpatterns = [
    path("", views.index, name="index"),
    path("add-author/", MyFormView.as_view(), name="new-form"),
    path("contact/", views.contact),
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
    path("about/", AboutView.as_view()),
]
