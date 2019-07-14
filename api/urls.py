from django.urls import path

from . import views

urlpatterns = [
    path('add-asset/', views.add_asset, name="add_asset"),
    path('add-task/', views.add_task, name="add_task"),
    path('add-worker/', views.add_worker, name="add_worker"),
    path('assets/all/', views.get_all_assets, name="get_all_assets"),
    path('allocate-task/', views.allocate_task, name="allocate_task"),
    path('worker/<str:worker_id>/', views.get_worker_task, name="worker_task"),
    path('worker/<str:worker_id>/view/', views.get_worker_taskview),
]
