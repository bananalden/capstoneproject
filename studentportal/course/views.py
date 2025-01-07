from django.shortcuts import render, redirect, HttpResponse
from course.forms import add_course
from course.models import Course

# Create your views here.
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
        valuesOfstuff = request.POST
        print(valuesOfstuff.cleaned_data)
        return HttpResponse('test')

def create_semester(request):
    return render(request, 'createsemester.html')

def create_subject(request):
    return render(request, 'createsubject.html')
