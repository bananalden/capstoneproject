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
            return redirect('admin:course:course-list')
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
            return redirect('admin:course:course-list')

    
def delete_course(request):
    if request.method =="POST":
        course_id = request.POST['delete_id']
        obj = get_object_or_404(Course, id=course_id)
        obj.delete()
        return redirect('admin:course:course-list')
        


#COURSE CRUD ACTION END


#SEMESTER CRUD ACTION START

def create_semester(request):
    form = add_semester()
    semesters = Semester.objects.all()
    if request.method == "POST":
        form = add_semester(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin:course:semester-list')
        
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
        return redirect('admin:course:semester-list')
        


#SEMESTER CRUD ACTION END

#SUBJECT CRUD ACTION START
def create_subject(request):
    form = add_subject()
    subjects = Subject.objects.all()
    if request.method == 'POST':
        f = add_subject(request.POST)
        if f.is_valid():
            f.save()
            return redirect('admin:course:subject-list')
        
    else:
        context = {'form':form,
                   'subjects': subjects
                   }                  
        return render(request, 'createsubject.html', context)
    
def update_subject(request):
    if request.method =="POST":
        subject_id = request.POST.get("edit_id")      
        obj = get_object_or_404(Subject, id=subject_id)
        f = add_subject(request.POST, instance=obj)
        if f.is_valid():
            f.save()
            return redirect('admin:course:subject-list')
        
def delete_subject(request):
    if request.method =="POST":
        semester_id = request.POST['delete_id']
        obj = get_object_or_404(Subject, id=semester_id)
        obj.delete()
        return redirect('admin:course:subject-list')
#SUBJECT CRUD ACTION END