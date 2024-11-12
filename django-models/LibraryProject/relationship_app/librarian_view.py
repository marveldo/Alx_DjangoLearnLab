from django.http import HttpResponseForbidden
from django.shortcuts import render


def Librarian(request):
    if request.user.userprofile.role != 'Librarian' :
        return HttpResponseForbidden()
    return render(request, 'relationship_app/librarian.html')