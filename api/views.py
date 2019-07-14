from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST, require_GET
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.decorators import login_required

from .models import *

def return_json(request, json):
    return render(request, "json_view.html", {"json": json})

# Create your views here.
@require_POST
def add_asset(request):
    try:
        asset = Asset()
        asset.assetname = request.POST.get("assetname")
        asset.date_of_purchase = request.POST.get("date_of_purchase")
        asset.price = request.POST.get("price")
        asset.date_of_last_maintainence = request.POST.get("date_of_last_maintainence")
        asset.save()
        return return_json(request, {"success": True})
    except:
        return return_json(request, {"success": False})

@require_POST
def add_task(request):
    try:
        task = Task()
        task.taskname = request.POST.get("taskname")
        task.task_description = request.POST.get("task_description")
        if("(" in request.POST.get("asset") and ")" in request.POST.get("asset")):
            asset = request.POST.get("asset").split("(")[-1][:-1]
        task.asset = Asset.objects.get(pk=asset)
        task.save()
        return return_json(request, {"success": True})
    except:
        return return_json(request, {"success": False})

@require_POST
def add_worker(request):
    worker = Worker()
    worker.workername = request.POST.get("workername")
    worker.worker_address = request.POST.get("worker_address")
    worker.join_date = request.POST.get("join_date")
    worker.date_of_birth = request.POST.get("date_of_birth")
    worker.save()
    return return_json(request, {"success": True})

@require_GET
def get_all_assets(request):
    assets = list(Asset.objects.all().values())
    return return_json(request, assets)

@require_POST
def allocate_task(request):
    try:
        if("(" in request.POST.get("task") and ")" in request.POST.get("task")):
            task = request.POST.get("task").split("(")[-1][:-1]
        if("(" in request.POST.get("asset") and ")" in request.POST.get("asset")):
            asset = request.POST.get("asset").split("(")[-1][:-1]
        if("(" in request.POST.get("worker") and ")" in request.POST.get("worker")):
            worker = request.POST.get("worker").split("(")[-1][:-1]
        task = Task.objects.get(pk=task)
        task.asset = Asset.objects.get(pk=asset)
        task.worker = Worker.objects.get(pk=worker)
        task.time_to_be_performed_by = request.POST.get("tbpb")
        task.save()
        return return_json(request, {"success": True})
    except:
        return return_json(request, {"success": True})

@require_GET
def get_worker_task(request, worker_id):
    worker = Task.objects.filter(worker__workerid=worker_id)
    return return_json(request, list(worker.values()), safe=False)

def get_worker_taskview(request, worker_id):
    task = Task.objects.filter(worker__workerid=worker_id)
    return render(request, "view_worker_task.html", {"tasks": task})
