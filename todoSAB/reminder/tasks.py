from __future__ import unicode_literals

from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from reminder.models import Reminder
from django.core.exceptions import ObjectDoesNotExist

@shared_task
#@task
def exceuteTask(id):
    
    try:
        entry = Reminder.objects.get(pk=id)
        print("working with", entry.name, entry.email)
        
        #try:
        #    subject = 'Reminder'
        #    message = entry.name
        #    to_list = [entry.email]
        #    send_mail(subject, message, settings.EMAIL_HOST_USER, to_list, fail_silently=True)
        #finally:
        #    print("Unable to send an email", entry.name, entry.email)
        
    except ObjectDoesNotExist:
        print("object was delete", id)

    
    
    