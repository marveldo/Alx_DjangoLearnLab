from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import permission_required
from .models import Library
from .models import Book
from .forms import Bookform
from django.http import HttpResponseForbidden, HttpResponse

def register(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'relationship_app/login.html', context={'form':form})

def list_books(request):
    books = Book.objects.all()
    return render(request , 'relationship_app/list_books.html',context={'books':books})


def is_member(user):
    return user.userprofile.role != 'Member'

@user_passes_test(is_member)
def member_view(request):
    return render(request , 'relationship_app/member_view.html')


def is_admin(user):
    return user.userprofile.role == 'Admin' 
        
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

def is_librarian(user):
    return user.userprofile.role != 'Librarian' 

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

class LibraryDetailView(DetailView):

    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

class UserRegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'relationship_app/register.html'
    success_url = reverse_lazy('login')

@permission_required('relationship_app.can_view', raise_exception=True)
def view_author(request):
    return HttpResponse('Hello there')

@permission_required('relationship_app.can_edit',raise_exception=True)
def edit_author(request):
    return HttpResponse('Edit author')
@permission_required('relationship_app.can_delete', raise_exception=True)
def delete_author(request):
    return HttpResponse('Delete author')

@permission_required('relationship_app.can_create', raise_exception=True)
def create_author(request):
    return HttpResponse('Can create')

@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request) :
    form = Bookform()
    if request.method == 'POST':
        form = Bookform(request.POST)
        if form.is_valid():
            form.save()
    return render(request , 'relationship_app/add_book.html', context ={'form': form})

@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request , pk) :
    book = Book.objects.get(id = pk)
    if request.method == 'POST':
        book.delete()
    return render(request, 'relationship_app/delete_book.html')

@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, pk):
    book = Book.objects.get(id = pk)
    form = Bookform(instance=book)
    if request.method == 'POST':
        form = Bookform(request.POST, instance=book)
        if form.is_valid():
            form.save()
    return render(request , 'relationship_app/edit_book.html', context={'form': form})




    

