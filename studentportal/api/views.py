from django.shortcuts import render
from django.http import JsonResponse
from course import models
from django.contrib.auth import get_user_model

# Create your views here.
app_name = "api"
#COURSES START
def get_course_list(request):
    courses = models.Course.objects.all().values('id','name')
    return JsonResponse(list(courses), safe=False)

def get_coursedata(request, pk):
    obj = models.Course.objects.get(pk=pk)
    if obj:
        data ={
        'id': obj.id,
        'name':obj.name
    }
        return JsonResponse(data)
    return JsonResponse({'error':'Object not found'}, status=404)


#COURSES END

#SEMESTER START
def get_semester_list(request):
    semester = models.Semester.objects.all().values('id','semester_code','semester','year','course_id')
    return JsonResponse(list(semester), safe=False)


def get_semesterdata(request, pk):
    obj = models.Semester.objects.get(pk=pk)
    if obj:
        data ={
        'id': obj.id,
        'semester_code':obj.semester_code,
        'semester':obj.semester,
        'year':obj.year,
        'course_id':obj.course_id
    }
        return JsonResponse(data)
    return JsonResponse({'error':'Object not found'}, status=404)


#SEMESTER END

#SUBJECT START

def get_subjectdata(request, pk):
    obj = models.Subject.objects.get(pk=pk)
    if obj:
        data ={
        'id': obj.id,
        'name':obj.name,
        'course_id':obj.course_id,
        'semester_id':obj.semester_id
    }
        return JsonResponse(data)
    return JsonResponse({'error':'Object not found'}, status=404)

#SUBJECT END

#ADMIN USER START

def get_admindata(request,pk):
    obj = get_user_model()
    admin = obj.objects.get(pk=pk)
    if admin:
        data={
                'id':admin.id,
                'first_name':admin.first_name,
                'last_name':admin.last_name,
                'email':admin.email,
                'username':admin.username,
        }
        return JsonResponse(data)
    return JsonResponse({'error':'Object not found'}, status=404)

#ADMIN USER END