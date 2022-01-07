from django.shortcuts import render,redirect
from .forms import AgregarTarea

tareas = []
# Create your views here.
def home(request):
    context ={"tareas":tareas}
    return render(request,"todu/home.html",context)

def add(request):
    if request.method == "POST":
        form = AgregarTarea(request.POST)
        if form.is_valid():
            tarea = form.cleaned_data["tarea"]
            tareas.append(tarea)
            return redirect("homeURL")
    else:
        form = AgregarTarea()
    context = {"form":form}
    return render(request,"todu/add.html",context)
