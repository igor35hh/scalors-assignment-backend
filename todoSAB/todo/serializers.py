from __future__ import unicode_literals

from rest_framework import  serializers
from todo.models import Todo, Board

class TodoSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Todo
        fields = ('url', 'id', 'name', 'board', 'done')

class BoardSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Board
        depth = 1
        fields = ('url', 'id', 'name', 'boards')
        
class BoardListSerializer(serializers.HyperlinkedModelSerializer):
    num_todos = serializers.IntegerField(read_only=True)
    
    class Meta:
        model = Board
        fields = ('url', 'id', 'name', 'num_todos')