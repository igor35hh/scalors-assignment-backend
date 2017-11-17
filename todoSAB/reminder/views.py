# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from rest_framework import viewsets
from reminder.models import Reminder
from .serializers import ReminderSerializer

from rest_framework import status
from datetime import datetime, timedelta
from .tasks import exceuteTask
from rest_framework.response import Response
from django.http.response import HttpResponse
from django.http.response import JsonResponse
from todoSAB import dequeOfTasks

class ReminderViewSet(viewsets.ModelViewSet):
    queryset = Reminder.objects.all() 
    serializer_class = ReminderSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        
        time_run = datetime.utcnow() + timedelta(minutes=int(serializer.data['delay']))
        taskres = exceuteTask.apply_async((serializer.data['id'],), eta=time_run)
        dequeOfTasks.append({'id':taskres.id, 'data':{'name':serializer.data['name'], 'email':serializer.data['email']}})
        
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
def tasksQueue(request):
    el, status, delete = findTask()
    if delete:
        data = {'status':status, 'data':el['data']}
        dequeOfTasks.remove(el)
        return JsonResponse(data, safe=True)
    return HttpResponse(status=204)

def findTask():
    if dequeOfTasks:
        from celery.result import AsyncResult
        from todoSAB import celery_app
        for el in dequeOfTasks:
            result = AsyncResult(el['id'], app=celery_app)
            if result.successful():
                return el, result.state, True
            if result.failed():
                return el, result.state, True
    return None, None, False


