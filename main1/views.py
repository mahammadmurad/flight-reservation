from django.shortcuts import render
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination

class AuthorPagination(PageNumberPagination):
    page_size = 2


class AuthorPaginationLimit(LimitOffsetPagination):
    default_limit = 3
    max_limit = 50


class AuthorListCreateView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    # pagination_class = PageNumberPagination
    # pagination_class = AuthorPagination
    # pagination_class = LimitOffsetPagination
    pagination_class = AuthorPaginationLimit

class AuthorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
