from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.


class UserResource(models.Model):
    user_id = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    imageUrl = models.CharField(max_length=255)
