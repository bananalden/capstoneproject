from django.shortcuts import render, redirect
from course.forms import add_course

# Create your views here.
def create_course(request):
    form = add_course()
    if request.method == 'POST':
        if form.is_valid():
            form.save(request.POST)
            return redirect('/schoolmanagement/course-list')
    else:
        context = {'form' : form}
        return render(request, 'createcourse.html', context)

def create_semester(request):
    return render(request, 'createsemester.html')

def create_subject(request):
    return render(request, 'createsubject.html')
