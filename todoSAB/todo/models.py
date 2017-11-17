# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Board(models.Model):
    name    = models.CharField(max_length=200, db_index=True, verbose_name='Title')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Board'
        verbose_name_plural = 'Boards'
        index_together = [
            ['id']
        ]
        
    def __str__(self):
        return self.name
    
class Todo(models.Model):
    name      = models.CharField(max_length=200, db_index=True, verbose_name='Title')
    board      = models.ForeignKey(Board, related_name='boards', on_delete=models.CASCADE)
    done       = models.BooleanField(default=False, verbose_name='Done')
    created   = models.DateTimeField(auto_now_add=True)
    updated  = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Todo'
        verbose_name_plural = 'Todos'
        index_together = [
            ['id']
        ]

    def __str__(self):
        return self.name
