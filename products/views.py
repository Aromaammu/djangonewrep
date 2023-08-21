from django.shortcuts import render
from django.http import HttpResponse
from .models import Nevin

# Create your views here.
def home(request):
    x=Nevin.objects.all()
    return render(request,"index.html",{'x':x})
