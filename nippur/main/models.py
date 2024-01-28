from django.db import models


class User(models.Model):
    username = models.CharField(max_length=10)
    password = models.CharField(max_length=10)
    email = models.EmailField(default = "example@e-mail.com")
    r_password = models.CharField(max_length=10)

    def __str__(self):
        return self.username


class Song(models.Model):
    title = models.CharField(max_length=100)
    file_path = models.FileField()



# Create your models here.

