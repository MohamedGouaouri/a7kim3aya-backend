from django.db import models
from django.urls import reverse

# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField()
    price = models.FloatField()

    def get_absolute_url(self):
        return reverse("show", kwargs={"pk": self.pk})
