# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.db import models

class Reminder(models.Model):
    name      = models.CharField(max_length=200, db_index=True, verbose_name='Title')
    email      = models.EmailField(max_length=70, verbose_name='Email')
    delay      = models.IntegerField(verbose_name='Minutes')
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
