# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from todo.models import Todo, Board
from django.db.models import Count
from rest_framework import viewsets
from .serializers import TodoSerializer, BoardSerializer, BoardListSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all() 
    serializer_class = TodoSerializer
    
class BoardViewSet(viewsets.ModelViewSet): 
    
    def list(self, request):
        queryset = Board.objects.annotate(num_todos=Count('boards')).all()
        serializer = BoardListSerializer(queryset, context={'request': request}, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        board = get_object_or_404(Board, pk=pk)
        serializer = BoardSerializer(board, context={'request': request})
        return Response(serializer.data)
    
    queryset = Board.objects
    serializer_class = BoardListSerializer
    
def index(request):
    return render(request, 'api.html', {})
