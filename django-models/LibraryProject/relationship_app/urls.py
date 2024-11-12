from django.urls import path
from django.contrib.auth.views import LoginView,LogoutView
from .views import list_books ,LibraryDetailView,UserRegisterView , add_book,edit_book,delete_book, register
from .admin_view import admin_view
from .member_view import member_view
from .librarian_view import librarian_view

project = 'views.register'
urlpatterns = [
    path('books/', list_books , name='books'),
    path('books/<int:pk>/', LibraryDetailView.as_view(), name='book_detail'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('admin/',admin_view, name='Admin'),
    path('librarian/', librarian_view, name='Librarian'),
    path('member/', member_view, name='Member' ),
    path('add_book/', add_book, name='add-book'),
    path('edit_book/<int:pk>/', edit_book, name='edit-book'),
    path('delete_book/<int:pk>/', delete_book , name='delete-book')

]