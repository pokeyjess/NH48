from django.shortcuts import render
from nh48_user.models import NHUser

def index(request):
    return render(request, "index.html")

def member(request, username):
    member_info = NHUser.objects.filter(username=username).first()
    return render(request, "member_profile.html", {"member": member_info})
