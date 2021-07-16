from django.db import models

class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    photo = models.TextField()
    bio = models.TextField()

    def __str__(self):
        return self.username

class Band(models.Model):
    band_name = models.CharField(max_length=100)
    photo = models.TextField()
    about = models.CharField(max_length=200)
    genre = models.CharField(max_length=100)
    music_url = models.TextField()

    def __str__(self):
        return self.band_name

class Message(models.Model):
    content = models.CharField(max_length=200)

    def __str__(self):
        return self.content