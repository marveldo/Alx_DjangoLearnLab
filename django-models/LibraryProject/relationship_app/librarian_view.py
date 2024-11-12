from django.http import HttpResponseForbidden
from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test

def is_librarian(user):
    return user.userprofile.role != 'Librarian' 

@user_passes_test(is_librarian)
def Librarian(request):
    return render(request, 'relationship_app/librarian.html')