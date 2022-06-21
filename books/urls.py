from django.urls import path
# from . import views
from books import views

app_name='books'
urlpatterns = [
    path('', views.index),
    path('details/<int:id>', views.detail, name='book-details'),
    path('details/author/<int:author_id>', views.author_details, name='author-details'),
    path('search/', views.search),                                                                   
    path('contact/', views.contact),
    path('add-author/', views.add_author),
]