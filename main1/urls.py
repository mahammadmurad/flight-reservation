from django.urls import path
from . import views

urlpatterns = [
    path("author/", views.AuthorListCreateView.as_view()),
    path("author/<int:pk>/", views.AuthorDetailView.as_view()),
    path("book/", views.BookListCreateView.as_view()),
    path("book/<int:pk>/", views.BookDetailView.as_view()),
]
