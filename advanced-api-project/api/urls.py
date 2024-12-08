from django.urls import path
from .views import ListView , CreateView , UpdateView , DetailView , DeleteView

urlpattterns = [
    path('books/', ListView.as_view()),
    path('books/<int:pk>/', DetailView.as_view()),
    path('books/', CreateView.as_view()),
     path('books/<int:pk>/', UpdateView.as_view()),
      path('books/<int:pk>/', DeleteView.as_view()),
]