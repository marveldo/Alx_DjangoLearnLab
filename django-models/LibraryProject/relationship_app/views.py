from django.shortcuts import render
from django.views.generic import DetailView, CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import user_passes_test , permission_required
from .models import Library
from .models import Book
from .forms import Bookform



def list_books(request):
    books = Book.objects.all()
    return render(request , 'relationship_app/list_books.html',context={'books':books})

class Librarydetail(DetailView):

    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

class UserRegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'relationship_app/register.html'
    success_url = reverse_lazy('login')

@user_passes_test(lambda user: user.profile.role == 'Admin')
def admin_view(request):
    return render(request, 'relationship_app/admin.html')

@user_passes_test(lambda user : user.profile.role == 'Librarian' )
def librarian_view(request):
    return render(request, 'relationship_app/librarian.html')

@user_passes_test(lambda user : user.profile.role == 'Member')
def member_view(request):
    return render(request , 'relationship_app/member.html')

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




    

