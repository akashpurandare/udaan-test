from django.db import models

import uuid
# Create your models here.

def get_uuid():
    """Make the UUID of 32 ascii characters, instead of 36, with 4 hyphens"""
    return "".join(str(uuid.uuid4()).split("-"))

# Register your models here.
class Asset(models.Model):
    assetid = models.CharField(primary_key=True, editable=False, max_length=255, default=get_uuid)
    assetname = models.CharField(max_length=255, verbose_name="Asset Name")
    date_of_purchase = models.DateField()
    price = models.FloatField()
    date_of_last_maintainence = models.DateTimeField()

    def __str__(self):
        return self.assetname+"("+self.assetid+")"

    class Meta:
        verbose_name = "Asset"
        verbose_name_plural = "Assets"

class Worker(models.Model):
    workerid = models.CharField(primary_key=True, editable=False, max_length=255, default=get_uuid)
    workername = models.CharField(max_length=255)
    worker_address = models.TextField()
    join_date = models.DateField()
    date_of_birth = models.DateField()

    def __str__(self):
        return self.workername+"("+self.workerid+")"

class Task(models.Model):
    taskid = models.CharField(primary_key=True, editable=False, max_length=255, default=get_uuid)
    taskname = models.CharField(max_length=255)
    task_description = models.TextField()
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    worker = models.ForeignKey(Worker, on_delete=models.SET_NULL, blank=True, null=True)
    time_of_allocation = models.DateTimeField(auto_now=True)
    time_to_be_performed_by = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        if self.worker:
            return self.taskname+" assigned to "+str(self.worker.workername)
        return self.taskname
