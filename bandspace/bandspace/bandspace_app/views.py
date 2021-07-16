from django.http.response import HttpResponsePermanentRedirect
from django.shortcuts import render
from django.core.serializers import serialize
from django.http import HttpResponse

from .models import User, Band, Message

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

def get_messages(request):
    messages = Message.objects.all()
    parsed_messages = serialize("json", messages)
    return HttpResponse(parsed_messages, content_type="application/json")

def create_message(request, upk):
    parsed_body = request.body.decode('utf-8')
    parsed_body = json.loads(parsed_body)
    print(parsed_body)

    message = Message(content=parsed_body['data'])
    message.save()

    parsed_message = serialize('json', [message])

    return HttpResponse(parsed_message, content_type="application/json")

def create_band(request, upk):
    parsed_body = request.body.decode('utf-8')
    parsed_body = json.loads(parsed_body)
    print(parsed_body)

    band = Band(band_name=parsed_body['data'])
    bandname = Band(band['band_name'])
    print(bandname)
    # photo = Band(photo=parsed_body['photo'])
    band.save()
    # photo.save()

    parsed_band = serialize('json', [band])

    return HttpResponse(parsed_band, content_type="application/json")

def create_user(request, upk):
    parsed_body = request.body.decode('utf-8')
    parsed_body = json.loads(parsed_body)

    user = User(bio=parsed_body['data'])

    user.save()

    parsed_user = serialize('json', [user])

    return HttpResponse(parsed_user, content_type="application/json")