from django.shortcuts import render
from django.db.models import Sum

from django.http import HttpResponse

from .models import Run

def index(request):
    distance = Run.objects.aggregate(Sum('duration'))
    output = str(distance)
    return HttpResponse(output)