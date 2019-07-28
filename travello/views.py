from django.shortcuts import render
from .models import Destination

# Create your views here.

# def index(request):
#     return render(request,"index.html",)

def index(request):
    # return render(request,"home.html",{"name":"Krishna"})
      

      dests=Destination.objects.all()

      return render(request,"index.html",{'dests':dests})
    