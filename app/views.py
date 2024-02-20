from django.shortcuts import render

# Create your views here.
def virat(request):
    return render(request,'virat.html')

def srk(request):
    return render(request,'srk.html')

def panda(request):
    return render(request,'panda.html')