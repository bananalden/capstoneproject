from django.shortcuts import render
from .forms import GeneralUserCreationForm

# Create your views here.

def index(request):
    form = GeneralUserCreationForm()
    if request.method == 'POST':
        form = GeneralUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print(form.errors.as_data())



    context = {'form': form}
    return render(request, 'test/usercreation.html', context)

def studentview(request):
    return render(request, 'studentside/index.html')

def registrarview(request):
    return render(request, 'registrar/index.html')

def cashierrview(request):
    return render(request, 'cashier/index.html')