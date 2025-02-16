from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from users import models as user_data
from news import models as news_data

# Create your views here.
app_name = "api"





#USER GRABBING START

def get_userdata(request,pk):
    try:
        user = get_user_model().objects.get(pk=pk)

        if user:
            data = {
                'id': user.id,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'email': user.email,
                'username': user.username,
            }

    
        return JsonResponse(data)


    except:
        return(JsonResponse({'error':'User not found'}, status=404))

#USER GRABBING END

#NEWS GRABBING START

def news_list(request):
    announcements = news_data.Announcement.objects.all()
    
    announcement_data = [
        {
            "id": announcement.id,
            "title": announcement.title,
            "body": announcement.body,
            "created_on": announcement.created_on.strftime("%Y-%m-%d"),
            "modified_on": announcement.modified_on.strftime("%Y-%m-%d"),
            "author": f"{announcement.author.first_name} {announcement.author.last_name}",
            "formatted_date": announcement.created_on.strftime("%B %d, %Y %I:%M %p"), 
        }
        for announcement in announcements
    ]

    return JsonResponse(announcement_data, safe=False)
        


#NEWS GRABBING END