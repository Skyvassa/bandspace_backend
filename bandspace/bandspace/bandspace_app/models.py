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
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bands', default=0)
    band_name = models.CharField(max_length=100)
    photo = models.TextField()
    about = models.CharField(max_length=200)
    genre = models.CharField(max_length=100)
    music_url = models.TextField()

    def __str__(self):
        return self.band_name

class UserFavBand(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='userfavbands')
    band = models.ForeignKey(Band, on_delete=models.CASCADE, related_name='bandfavusers')

    def __str__(self):
        return self.band.band_name