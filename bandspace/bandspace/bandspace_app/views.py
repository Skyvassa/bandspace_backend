from django.shortcuts import render
from django.core.serializers import serialize
from django.http import HttpResponse

from .models import User, Band

import json

def band_list(request):
    bands = Band.objects.all()
    return render(request, 'bandspace/band_list.html', {'bands':bands})

# Create your views here.
