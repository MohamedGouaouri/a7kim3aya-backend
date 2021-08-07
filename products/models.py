from django.db import models
from django.urls import reverse

# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField()
    price = models.FloatField()

    def get_absolute_url(self):
        return reverse("show", kwargs={"pk": self.pk})


# For the sake of learning about django models
# ManyToone relation ship
class ManuFactorar(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()


class Car(models.Model):
    name = models.CharField(max_length=20)
    # Many to one relationship
    manufactorar = models.ForeignKey(ManuFactorar, on_delete=models.CASCADE)


# Many-to-many relation

class Course(models.Model):
    name = models.CharField(max_length=20)
    credit = models.IntegerField()


class Teacher(models.Model):
    name = models.CharField(max_length=20)
    teaches = models.ManyToManyField(Course, through='Syllabus')


class Syllabus(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
