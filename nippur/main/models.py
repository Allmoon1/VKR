from django.db import models


class User(models.Model):
    username = models.CharField(max_length=10)
    password = models.CharField(max_length=10)
    email = models.EmailField(default = "example@e-mail.com")
    r_password = models.CharField(max_length=10)

    def __str__(self):
        return self.username


class Song(models.Model):
    num = models.IntegerField()
    song_id = models.CharField(max_length=20)
    title = models.TextField()
    cluster = models.IntegerField()
    file_path = models.FileField()

    def get_title(self):
        return str(self.title)
    def get_path(self):
        return str(self.file_path)

# Create your models here.

