from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponse
from .forms import ExampleForm,Book

# Create your views here.
listed = ["book_list", "books"]
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

def example_view(request):
    form = ExampleForm()
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'bookshelf/form_example.html', context={'form' : form})

def booklist(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', context={'books': books})