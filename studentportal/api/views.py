from django.shortcuts import render
from django.http import JsonResponse
from course import models as course_data
from django.contrib.auth import get_user_model
from users import models as user_data

# Create your views here.
app_name = "api"
#COURSES START
def get_course_list(request):
    courses = course_data.Course.objects.all().values('id','name')
    return JsonResponse(list(courses), safe=False)

def get_coursedata(request, pk):
    obj = course_data.Course.objects.get(pk=pk)
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
    semester = course_data.Semester.objects.all().values('id','semester_code','semester','year','course_id')
    return JsonResponse(list(semester), safe=False)


def get_semesterdata(request, pk):
    obj = course_data.Semester.objects.get(pk=pk)
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
    obj = course_data.Subject.objects.get(pk=pk)
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

#USER GRABBING START

def get_userdata(request,pk):
    try:
        user = get_user_model().objects.get(pk=pk)

        try:
            teacher_course = user_data.TeacherProfile.objects.get(teacher_id=pk)
            data = {
                'id':user.id,
                'first_name':user.first_name,
                'last_name':user.last_name,
                'email':user.email,
                'username':user.username,
                'course_id':teacher_course.course_id
            }
        except user_data.TeacherProfile.DoesNotExist:
            data = {
                'id':user.id,
                'first_name':user.first_name,
                'last_name':user.last_name,
                'email':user.email,
                'username':user.username,
            }
        return JsonResponse(data)


    except:
        return(JsonResponse({'error':'User not found'}, status=404))

#USER GRABBING END
