from django.db import models

# Create your models here.


class Blogger(models.Model):
    class Meta:
        db_table = "blogger"

    name = models.CharField(max_length=200)
    email = models.EmailField()
    age = models.IntegerField(default=20)

    def to_json_format(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'age': self.age
        }

    def __str__(self) -> str:
        return self.name


class Blog(models.Model):
    class Meta:
        db_table = "blog"

    name = models.CharField(max_length=100)
    body = models.TextField()
    tagline = models.TextField()
    blogger = models.ForeignKey(Blogger, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.name
