from django.http import HttpResponseForbidden
from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test


def is_member(user):
    return user.userprofile.role != 'Member'
@user_passes_test(is_member)
def Member(request):
    return render(request , 'relationship_app/member.html')