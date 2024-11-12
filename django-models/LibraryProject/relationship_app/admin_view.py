from django.http import HttpResponseForbidden
from django.shortcuts import render

def Admin(request):
    if request.user.userprofile.role != 'Admin' :
        return HttpResponseForbidden()
    return render(request, 'relationship_app/admin.html')