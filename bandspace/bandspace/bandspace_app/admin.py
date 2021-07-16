from django.contrib import admin
from .models import User, Band, Message

admin.site.register(User)
admin.site.register(Band)
admin.site.register(Message)