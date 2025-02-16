from django.utils.timezone import now
from django.shortcuts import render,redirect
from news.models import Announcement
import pytz

# Create your views here.
def create_announcements(request):
    if request.method == "POST":
        title = request.POST.get("title")
        body = request.POST.get("body")

        if title and body:
            manila_timezone = pytz.timezone('Asia/Manila')
            now_ph = now().astimezone(manila_timezone)

            Announcement.objects.create(title=title, body=body, author=request.user, created_on=now_ph, modified_on=now_ph)
            print("Succesfully created announcement")
            return redirect('home:teacher-newsfeed')
        else:
            print("whatareyastupid")
            return redirect('home:teacher-newsfeed')