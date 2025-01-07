from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse
from course.forms import add_course
from course.models import Course
from django.shortcuts import get_object_or_404

# Create your views here.

#COURSE CRUD ACTION START
def create_course(request):

    form = add_course()
    course = Course.objects.all()
    if request.method == 'POST':
        f = add_course(request.POST)
        if f.is_valid():
            f.save()
            return redirect('course:course-list')
    else:
        context = {'form' : form,
                   'course': course
                   }
        return render(request, 'createcourse.html', context)

def update_course(request):
    if request.method =="POST":
        course_id = request.POST.get("id")      
        obj = get_object_or_404(Course, id=course_id)
        f = add_course(request.POST, instance=obj)
        if f.is_valid():
            f.save()
            return redirect('course:course-list')

    
def delete_course(request):
    if request.method =="POST":
        course_id = request.POST['delete_id']
        obj = get_object_or_404(Course, id=course_id)
        obj.delete()
        return redirect('course:course-list')
        

def get_coursedata(request, pk):
    obj = Course.objects.get(pk=pk)
    if obj:
        data ={
        'id': obj.id,
        'name':obj.name
    }
        return JsonResponse(data)
    return JsonResponse({'error':'Object not found'}, status=404)


#COURSE CRUD ACTION END

def create_semester(request):
    return render(request, 'createsemester.html')

def create_subject(request):
    return render(request, 'createsubject.html')
