from django.db import models

# Create your models here.
class Student(models.Model):
    Firstname = models.CharField(max_length=50)
    Lirstname = models.CharField(max_length=50)
    Email = models.EmailField()
    Contact = models.CharField(max_length=15)

    def __str__(self) -> str:
        return self.Firstname
