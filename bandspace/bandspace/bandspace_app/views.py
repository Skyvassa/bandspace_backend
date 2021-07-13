from django.http.response import HttpResponsePermanentRedirect
from django.shortcuts import render
from django.core.serializers import serialize
from django.http import HttpResponse

from .models import User, Band

import json

def get_bands(request):
    bands = Band.objects.all()
    parsed_bands = serialize("json", bands)
    return HttpResponse(parsed_bands, content_type="application/json")
    # return render(request, 'bandspace/get_bands.html', {'bands':bands})

def get_users(request):
    users = User.objects.all()
    parsed_users = serialize("json", users)
    return HttpResponse(parsed_users, content_type="application/json")

def get_user(request, pk):
    user = User.objects.get(id=pk)
    parsed_user = serialize("json", [user])
    return HttpResponse(parsed_user, content_type="application/json")

def create_user(request, upk):
    parsed_body = request.body.decode('utf-8')
    parsed_body = json.loads(parsed_body)

    user = User(content=parsed_body['data'])
    user.save()

    parsed_user = serialize('json', [user])

    return HttpResponse(parsed_user, content_type="application/json")