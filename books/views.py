from django.shortcuts import render
from rest_framework import viewsets
from .serializers import AuthorSerializer, BooksSerializer
from .models import Author, Books
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class AuthorViewset(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = ( IsAuthenticatedOrReadOnly, )
    
class BooksViewset(viewsets.ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer
    permission_classes = ( IsAuthenticatedOrReadOnly, )
