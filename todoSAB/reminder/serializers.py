from __future__ import unicode_literals

from rest_framework import  serializers
from reminder.models import Reminder

class ReminderSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Reminder
        fields = ('url', 'id', 'name', 'email', 'delay', 'created')