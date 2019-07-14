"""udaan URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('asset/', views.add_asset, name="addassetview"),
    path('task/', views.add_task, name="taskview"),
    path('worker/', views.add_worker, name="workerview"),
    path('allocate/', views.allocate_task, name="allocateview"),
    path('view_assets', views.view_assets, name="assetview"),
    path('view_worker/', views.get_worker_tasks, name="workertaskview"),
    path('', views.home, name="homepage"),
    path('', include('api.urls')),
]
