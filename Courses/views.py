from django.shortcuts import render
from .models import Cours

# Create your views here.




def cours_list(request):
    all=Cours.objects.all()
    return render(request,'courses.html',{'data':all})




def cours_detail(request,id):
    cours=Cours.objects.get(id=id)
    return render (request,'single.html',{'data':cours})
