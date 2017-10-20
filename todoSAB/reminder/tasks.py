from __future__ import unicode_literals

from celery import task, shared_task

@shared_task
#@task
def exceuteTask(arg):
    print("1111111111111111111111")