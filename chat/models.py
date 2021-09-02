from django.db import models
from django.contrib.auth import get_user_model
from django.utils.timezone import now
from django.db.models import constraints

from django.db.models.constraints import CheckConstraint
from django.db.models import F
from django.db.models.query_utils import Q

# Create your models here.


# This class is used to create the database table for the ChatUser model
# It inherits from the django.db.models.Model class
class UserResource(models.Model):
    user_id = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    imageUrl = models.CharField(max_length=255)
    roomPartialCode = models.IntegerField(unique=True, default=0)


class Message(models.Model):

    message_from = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name='message_from', name='message_from')
    message_to = models.ForeignKey(get_user_model(
    ), on_delete=models.CASCADE, related_name='message_to', name='message_to')
    content = models.TextField(max_length=1000)
    at = models.DateTimeField(default=now())

    def __repr__(self) -> str:
        return f"Message ({self.id}) from {self.message_from.username} to {self.message_to.username}"
