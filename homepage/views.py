from django.shortcuts import render
from .models import Cell

def home(request):
    cells=Cell.objects.all()
    context={
        'cells':cells,
    }
    return render(request,'homepage/home.html',context)
