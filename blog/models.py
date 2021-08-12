from django.db import models

# Create your models here.


class Blogger(models.Model):
    class Meta:
        db_table = "blogger"

    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self) -> str:
        return self.name


class Blog(models.Model):
    class Meta:
        db_table = "blog"

    name = models.CharField(max_length=100)
    body = models.TextField()
    tagline = models.TextField()
    blogger = models.ForeignKey(Blogger, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name
