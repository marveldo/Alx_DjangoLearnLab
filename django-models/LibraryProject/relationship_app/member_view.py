from django.http import HttpResponseForbidden
from django.shortcuts import render


def Member(request):
    if request.user.userprofile.role != 'Member' :
        return HttpResponseForbidden()
    return render(request , 'relationship_app/member.html')