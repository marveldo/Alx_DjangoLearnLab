from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponse

# Create your views here.
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