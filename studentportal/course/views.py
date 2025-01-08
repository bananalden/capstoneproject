from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse
from course.forms import add_course, add_semester, add_subject
from course.models import Course, Semester, Subject
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

def get_course_list(request):
    courses = Course.objects.all().values('id','name')
    return JsonResponse(list(courses), safe=False)


#COURSE CRUD ACTION END


#SEMESTER CRUD ACTION START

def create_semester(request):
    form = add_semester()
    semesters = Semester.objects.all()
    if request.method == "POST":
        form = add_semester(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course:semester-list')
        
    else:
         context = {'form': form,
                    'semesters': semesters
                    }
         return render(request, 'createsemester.html', context)

def update_semester(request):
    if request.method =="POST":
        semester_id = request.POST.get("id")      
        obj = get_object_or_404(Semester, id=semester_id)
        f = add_semester(request.POST, instance=obj)
        if f.is_valid():
            f.save()
            return redirect('course:semester-list')
        
def delete_semester(request):
    if request.method =="POST":
        semester_id = request.POST['delete_id']
        obj = get_object_or_404(Semester, id=semester_id)
        obj.delete()
        return redirect('course:semester-list')
        


def get_semesterdata(request, pk):
    obj = Semester.objects.get(pk=pk)
    if obj:
        data ={
        'id': obj.id,
        'semester':obj.semester,
        'year':obj.year,
        'course_id':obj.course_id
    }
        return JsonResponse(data)
    return JsonResponse({'error':'Object not found'}, status=404)

#SEMESTER CRUD ACTION END

#SUBJECT CRUD ACTION START
def create_subject(request):
    form = add_subject()
    subjects = Subject.objects.all()
    if request.method == 'POST':
        f = add_subject(request.POST)
        if f.is_valid():
            f.save()
            return redirect('course:subject-list')
        
    else:
        context = {'form':form,
                   'subjects': subjects
                   }                  
        return render(request, 'createsubject.html', context)
#SUBJECT CRUD ACTION END