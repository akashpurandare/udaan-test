from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from api.models import *

def home(request):
    return render(request, "base.html")

def add_asset(request):
    return render(request, "add_asset.html")

def add_task(request):
    assets = Asset.objects.all()
    return render(request, "add_task.html", {"assets": assets})

def add_worker(request):
    return render(request, "add_worker.html")

def view_assets(request):
    assets = Asset.objects.all()
    return render(request, "view_assets.html", {"assets": assets})

def allocate_task(request):
    assets = Asset.objects.all()
    workers = Worker.objects.all()
    tasks = Task.objects.all()
    return render(request, "allocate_task.html", {"assets": assets, "workers": workers, "tasks": tasks})

def get_worker_tasks(request):
    workers = Worker.objects.all()
    return render(request, "view_worker.html", {"workers": workers})
