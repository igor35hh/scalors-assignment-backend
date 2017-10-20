# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from rest_framework import viewsets
from reminder.models import Reminder
from .serializers import ReminderSerializer

from rest_framework import status
from rest_framework.response import Response
from datetime import datetime, timedelta
from .tasks import exceuteTask

class ReminderViewSet(viewsets.ModelViewSet):
    queryset = Reminder.objects.all() 
    serializer_class = ReminderSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        
        time_run = datetime.utcnow() + timedelta(minutes=int(serializer.data['delay']))
        exceuteTask.apply_async((serializer.data['id'],), eta=time_run)
        
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
