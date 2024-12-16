from django.shortcuts import render


# Create your views here.

def index(request):

    return render(request, 'test/usercreation.html')

def studentview(request):
    return render(request, 'studentside/index.html')

def registrarview(request):
    return render(request, 'registrar/index.html')

def cashierrview(request):
    return render(request, 'cashier/index.html')