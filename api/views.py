from django.shortcuts import render
from .models import *
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse


# Create your views here.

def StudentView(request):
    stu = Student.objects.all() ## complex data
    print(stu)
    serializer = StudentSerializer(stu, many= True) ## Python data
    json_data = JSONRenderer().render(serializer.data) ## Json data

    return HttpResponse(json_data,content_type='application/json')