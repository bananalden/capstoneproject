from django.shortcuts import render,redirect
from news.models import Announcement

# Create your views here.
def create_announcements(request):
    if request.method == "POST":
        title = request.POST.get("title")
        body = request.POST.get("body")

        if title and body:
            Announcement.objects.create(title=title, body=body, author=request.user)
            print("Succesfully created announcement")
            return redirect('home:teacher-newsfeed')
        else:
            print("whatareyastupid")
            return redirect('home:teacher-newsfeed')