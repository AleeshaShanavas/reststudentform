from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from .serializer import BookSerializer, AuthorSerializer
from .models import Book, Author


class BookView(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()


class AuthorView(viewsets.ModelViewSet):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()