from django.shortcuts import render, redirect

from .forms import ProjectsForm
from .models import Projects
# Create your views here.


def index(request):
    projects = Projects.objects.all()

    return render(request, "main/index.html", {"title": "Главная страница сайта", "projects": projects})


def about(request):
    return render(request, "main/about.html")


def create(request):
    error = ""
    if request.method == "POST":
        form = ProjectsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
        else:
            error = "Неверные значения"

    form = ProjectsForm()
    context = {
        "form": form,
        "error": error
    }
    return render(request, "main/create.html", context)
