from __future__ import absolute_import, unicode_literals

from ._celery import app as celery_app
from collections import deque

dequeOfTasks = deque()

__all__ = ['celery_app, dequeOfTasks']