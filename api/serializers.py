from rest_framework import serializers
from .models import *


# class StudentSerializer(serializers.ModelSerializer):
#     Firstname = models.CharField(max_length=50)
#     Lirstname = models.CharField(max_length=50)
#     Email = models.EmailField()
#     Contact = models.CharField(max_length=15)

from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
