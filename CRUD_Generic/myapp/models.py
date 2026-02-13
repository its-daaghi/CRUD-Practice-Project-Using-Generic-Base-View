from django.db import models

# Create your models here.
from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=100)
    roll = models.IntegerField(unique=True)
    marks = models.FloatField()

    def __str__(self):
        return f"{self.name} - {self.roll}"
