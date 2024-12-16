from django.shortcuts import render
from .forms import NewUserCreationForm

# Create your views here.

def index(request):

    if request.method != 'POST':
        form = NewUserCreationForm()

    else:
      form = NewUserCreationForm(request.POST)
      if form.is_valid():
          form.save()
          
    
    context = {'form': form}
    return render(request, 'test/usercreation.html', context)

def studentview(request):
    return render(request, 'studentside/index.html')

def registrarview(request):
    return render(request, 'registrar/index.html')

def cashierrview(request):
    return render(request, 'cashier/index.html')