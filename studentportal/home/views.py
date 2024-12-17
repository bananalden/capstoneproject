from django.shortcuts import render
from .forms import GeneralUserCreationForm

# Create your views here.

def index(request):
    form = GeneralUserCreationForm
    context = GeneralUserCreationForm()
    return render(request, 'test/usercreation.html', {'form': form})

def studentview(request):
    return render(request, 'studentside/index.html')

def registrarview(request):
    return render(request, 'registrar/index.html')

def cashierrview(request):
    return render(request, 'cashier/index.html')