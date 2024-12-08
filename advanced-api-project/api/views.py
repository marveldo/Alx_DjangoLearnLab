from django.shortcuts import render
from rest_framework import generics
from .serializers import Book ,BookSerializer 
from rest_framework.response import Response
from rest_framework import status
from rest_framework.filters import SearchFilter , OrderingFilter
from django_filters import rest_framework as filters 
# Create your views here.
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated IsAuthenticated

class ListView(generics.ListAPIView):
    # A listView to list all Books
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [SearchFilter , OrderingFilter, filters.DjangoFilterBackend]
    search_fields = ['title', 'author__name']  
    ordering_fields = ['title', 'publication_year'] 


class DetailView(generics.RetrieveAPIView):
    # A Detailview to get a specific book
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class CreateView(generics.CreateAPIView):
    # A createview to create a specific book
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def create(self, request, *args, **kwargs):
        # A create method to handle the creation of a book
        serializer = self.get_serializer(data = request.data)
        if serializer.is_valid(raise_exception = True):
            self.perform_create(serializer=serializer)
        return Response(status=status.HTTP_201_CREATED, data=serializer.data)

class UpdateView(generics.UpdateAPIView):
    # An update View to handle Updates of  a book
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def update(self, request, *args, **kwargs):
        # An update method to handle how the book is Updated
        instance = self.get_object()
        serializer = self.get_serializer(instance , data = request.data , partial =  True )
        if serializer.is_valid(raise_exception = True):
            self.perform_update(serializer=serializer)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

class DeleteView(generics.DestroyAPIView):
    # A view to handle deletion of books
    queryset = Book.objects.all()
    serializer_class = BookSerializer


