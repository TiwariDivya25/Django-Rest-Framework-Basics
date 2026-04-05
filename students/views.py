from django.shortcuts import render
from django.http import HttpResponse

def students(request):
    #web application endpoint e.g. /students/ will return a list of students in JSON format
    data = [{
        'name': 'John Doe',
        'age': 20,
        'grade': 'A'
    }]
    return HttpResponse(data)