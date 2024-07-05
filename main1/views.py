from django.shortcuts import render
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer
from rest_framework import generics
################################################################
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
################################################################
from rest_framework import filters
######################################
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions

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
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['first_name', 'last_name']
    ordering_fields = ['pk']
    # ordering = ['first_name']
    ###################################
    # authentication_classes = [BasicAuthentication] 
    # permission_classes = [IsAuthenticated, DjangoModelPermissions]

class AuthorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
