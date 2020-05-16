from django.shortcuts import render
from .models import *
# Create your views here.
def profilelist(request):
    template_name="profilelist.html"
    profile=profilelist.objects.all()
    return render(request, template_name, {"profile":profile})

def profiledetail(request):
    template_name=""
    return render(request, template_name, {})
    
    